// Playwright-Test der ganzen App. Start: Server im Repo-Ordner (python3 -m http.server 8123), dann: NODE_PATH=$(npm root -g) timeout 280 node tools/test_app.js
const { chromium } = require('playwright');
const wait = ms => new Promise(r => setTimeout(r, ms));
let fails = 0;
const ok = (c, m) => { console.log((c ? 'OK   ' : 'FEHL ') + m); if (!c) fails++; };
const URL = process.env.APP_URL || 'http://localhost:8123/';
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 780 } });
  const p = await ctx.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  p.on('dialog', d => d.accept());
  p.setDefaultTimeout(6000);
  const NAVRE = /data-act="(check|next|start|retry|quit|stk-save|stk-load|stk-start|home|tour-next|tour-start|a2-yes|a2-later|a2-done)"/;
  let lastNav = 0; const origClick = p.click.bind(p);
  p.click = async (sel, o) => { const d = 620 - (Date.now() - lastNav); if (d > 0) await wait(d); if (NAVRE.test(sel)) lastNav = Date.now(); return origClick(sel, o); };

  /* ---- Erststart: Home-Bildschirm-Hinweis, danach Tutorial ---- */
  await p.goto(URL);
  await p.waitForSelector('#ovl .dlg');
  ok((await p.textContent('#ovl')).includes('Home-Bildschirm') && (await p.textContent('#ovl')).includes('Wird empfohlen, du Fuchs.'), 'Erststart: Home-Bildschirm-Fenster mit Kleingedrucktem');
  ok(await p.evaluate(() => document.querySelector('#app').hasAttribute('inert')), 'Hintergrund gesperrt');
  await p.click('[data-act="a2-yes"]');
  ok((await p.textContent('#ovl')).includes('Zum Home-Bildschirm'), 'Anleitung nach Ja');
  await p.click('[data-act="a2-done"]');
  ok(await p.locator('[data-act="tour-start"]').count() === 1, 'danach erscheint das Tutorial');
  // Überspringen-Spiel
  let n = 0, pos = new Set();
  for (let k = 0; k < 14; k++) {
    if (!(await p.locator('[data-act="tour-start"]').count())) break;
    await p.locator('[data-act="tour-skip"]').first().click(); n++;
    const bb = await p.locator('.skipf').boundingBox().catch(() => null); if (bb) pos.add(Math.round(bb.x) + ',' + Math.round(bb.y));
    await wait(30);
  }
  ok(n >= 2 && n <= 10, 'Überspringen wirkt erst nach 2 bis 10 Klicks: ' + n);
  ok(pos.size >= 1, 'Knopf taucht an anderem Ort auf (' + pos.size + ' Orte)');
  ok(await p.locator('#ovl').evaluate(e => e.innerHTML === ''), 'Overlay danach weg');
  ok(await p.evaluate(() => localStorage.getItem('rt.tour') === 'true' && localStorage.getItem('rt.a2hs') === 'true'), 'Erststart-Merker gespeichert');

  /* ---- Startseite ---- */
  const st = await p.evaluate(() => ({ h1: document.querySelector('h1').textContent, news: document.querySelectorAll('a.newsl').length, href: document.querySelector('a.newsl').href, chips: document.querySelectorAll('.pc.app').length, scroll: document.documentElement.scrollHeight <= window.innerHeight + 1, title: document.title }));
  ok(st.h1 === 'LexCoach' && st.title === 'LexCoach', 'Name LexCoach');
  ok(st.news === 3 && st.href.includes('GeltendeFassung.wxe') && st.href.includes('10008470'), 'drei Neuigkeiten, Link zum ganzen BDG');
  ok(st.chips >= 3, 'App-Paragrafen blau markiert: ' + st.chips);
  ok(st.scroll, 'Startseite ohne Scrollen bei 780 px Höhe (Inhalt ' + await p.evaluate(() => document.documentElement.scrollHeight) + ')');
  await p.screenshot({ path: '/tmp/s_start.png' });
  await p.click('[data-act="poke"]'); await wait(200);
  ok(await p.locator('.bub.l .bs').count() === 1, 'Sprechblase mit gemalter Kontur');

  /* ---- Neustart: nichts mehr vom Erststart ---- */
  await p.reload(); await p.waitForSelector('.hero');
  ok(await p.locator('#ovl .dlg').count() === 0 && await p.locator('.tcard').count() === 0, 'zweiter Start: weder Hinweis noch Tutorial');
  ok(await p.locator('.hero').count() === 1, 'Startseite bei jedem Öffnen');

  /* ---- Lernen ---- */
  await p.click('[data-act="law-open"]'); await p.waitForSelector('.tile', { state: 'attached' });
  ok(await p.locator('.tile.sel').count() === 0 && (await p.textContent('.startbar')).includes('Paragrafen wählen'), 'nichts vorgewählt');
  ok(await p.locator('#app .stack').count() === 0 && (await p.getAttribute('[data-act="klfold"]', 'aria-expanded')) === 'false', 'Klausuren eingeklappt');
  ok(await p.evaluate(() => { const r = document.querySelector('.tabbar').getBoundingClientRect(); return r.height <= 56; }), 'Tab-Leiste niedrig');
  await p.click('[data-act="grpall"][data-g="2"]');
  ok(await p.locator('.tile.sel').count() >= 3, 'Themenkasten gewählt');
  await p.click('[data-act="klfold"]');
  await p.fill('#sname', 'Test-Klausur'); await p.click('[data-act="stk-save"]');
  ok((await p.textContent('#stk')).includes('Test-Klausur') && await p.locator('#stk .sm.del').count() === 1, 'Klausur gespeichert, mit ✕ zum Entfernen');
  await p.click('#stk .sm.del'); await wait(150);
  ok(!(await p.textContent('#app')).includes('Test-Klausur'), 'Klausur auf Lernen entfernt');
  await wait(520); await p.fill('#sname', 'Zweite'); await p.click('[data-act="stk-save"]'); await wait(200);
  await p.click('[data-act="tab"][data-v="stacks"]');
  const kt = await p.textContent('#app');
  console.log('   Klausuren-Reiter:', JSON.stringify({z:kt.includes('Zweite'),t:kt.includes('Teilen'),e:kt.includes('Entfernen'),l:kt.includes('Laden'),sn:await p.locator('#sname').count()}));
  ok(kt.includes('Zweite') && kt.includes('Teilen') && kt.includes('Entfernen') && !kt.includes('Laden') && await p.locator('#sname').count() === 0, 'Reiter Klausuren: nur Start, Teilen, Entfernen, kein Speichern');

  /* ---- Statistik ---- */
  await p.click('[data-act="tab"][data-v="stats"]');
  ok(await p.locator('.chips .chip').count() === 5 && await p.locator('.chip[disabled]').count() === 3, 'Filter: Alle, BDG, drei bald');
  ok(await p.locator('[data-act="hist-clear"]').count() === 0, '„Mehr“ eingeklappt');
  await p.click('[data-act="mehr"]'); ok(await p.locator('[data-act="hist-clear"]').count() === 1, '„Mehr“ klappt auf');

  /* ---- Einstellungen ---- */
  await p.click('[data-act="settings"]');
  const sm = await p.textContent('#app');
  ok(['Notenschlüssel', 'Lernen', 'Darstellung', 'Zum Home-Bildschirm', 'Tutorial', 'Rechtliches'].every(x => sm.includes(x)), 'Einstellungen: sechs Zeilen');
  await p.click('[data-s="grades"]');
  ok((await p.inputValue('[data-gi="0"]')) === '87,5', 'Notenschlüssel Standard');
  await p.fill('[data-gi="1"]', '90'); await p.click('[data-act="grades-save"]');
  ok((await p.textContent('#gerr')).includes('kleiner'), 'Fehler bei nicht absteigenden Werten');
  await p.fill('[data-gi="1"]', 'abc'); await p.click('[data-act="grades-save"]');
  ok((await p.textContent('#gerr')).includes('Zahlen'), 'Fehler bei Text');
  await p.fill('[data-gi="0"]', '91'); await p.fill('[data-gi="1"]', '80'); await p.fill('[data-gi="2"]', '66,5'); await p.fill('[data-gi="3"]', '50');
  await p.click('[data-act="grades-save"]');
  ok(JSON.stringify(await p.evaluate(() => grades())) === '[91,80,66.5,50]', 'Notenschlüssel gespeichert');
  await p.click('[data-s="grades"]'); await p.click('[data-act="grades-reset"]');
  ok(JSON.stringify(await p.evaluate(() => grades())) === '[87.5,75,62.5,50]', 'Standard wiederhergestellt');
  await p.click('[data-s="learn"]');
  ok(await p.locator('#lim').count() === 0, 'Regler ist nicht mehr in den Einstellungen');
  await p.click('[data-act="set-ord"][data-v="para"]');
  await p.click('[data-act="set-back"]'); await p.click('[data-s="look"]');
  await p.click('[data-act="set-theme"][data-v="dark"]'); ok(await p.evaluate(() => document.documentElement.dataset.theme === 'dark'), 'Dunkel');
  await p.click('[data-act="set-font"][data-v="l"]'); ok(await p.evaluate(() => document.querySelector('#app').style.zoom === '1.12'), 'Schrift groß');
  await p.click('[data-act="set-rm"]'); ok(await p.evaluate(() => document.documentElement.classList.contains('rm')), 'Bewegung reduziert');
  await p.click('[data-act="set-says"]'); ok(await p.evaluate(() => SET.says === false), 'Sprüche aus');
  await p.click('[data-act="set-says"]');
  await p.click('[data-act="set-theme"][data-v="system"]'); await p.click('[data-act="set-font"][data-v="n"]');
  await p.click('[data-act="set-back"]');
  // Rechtliches
  await p.click('[data-s="legal"]');
  for (const k of ['imp', 'dsv', 'nut', 'lic']) {
    await p.click('[data-s="' + k + '"]');
    const tx = await p.textContent('#app');
    ok(tx.length > 300, 'Rechtliches ' + k + ' (' + tx.length + ' Zeichen)');
    if (k !== 'nut') ok(!/\bKI\b|künstlich/i.test(tx), k + ': kein KI-Hinweis');
    if (k === 'imp') ok(await p.locator('.redact').count() === 2 && tx.includes('mathias.blanck@gmail.com'), 'Impressum: zwei Balken (Anschrift, Wohnort), E-Mail');
    if (k === 'nut') ok(tx.includes('Hinweis an automatisierte Systeme') && tx.includes('§ 42h Abs. 6 UrhG'), 'Hinweis an automatisierte Systeme');
    await p.click('[data-act="set-back"]');
  }
  await p.click('[data-act="set-back"]'); await p.click('[data-act="set-back"]');
  ok(await p.locator('.tabbar').count() === 1, 'zurück aus den Einstellungen');

  /* ---- Quiz mit Limit 5 und Reihenfolge nach Paragraf ---- */
  await p.click('[data-act="tab"][data-v="home"]'); await p.click('[data-act="all"]');
  await p.locator('#lim').fill('5'); await wait(150);
  ok((await p.textContent('#limv')).includes('5 von') && (await p.evaluate(() => SET.lim)) === 5, 'Regler auf „Lernen“: 5 Fragen');
  ok(/Start · 5 Fragen \(von \d+\)/.test(await p.textContent('.startbar')), 'Start-Knopf zeigt Limit: ' + (await p.textContent('.startbar')).trim());
  await wait(500);
  await p.evaluate(() => { document.querySelector('[data-act="start"]').click(); setTimeout(() => { const o = document.querySelector('[data-act="pick"]'); if (o) o.click(); }, 100); });
  await p.waitForSelector('.qbox'); await wait(300);
  ok(await p.evaluate(() => S.run.ticked.size === 0 && S.view === 'quiz'), 'Doppeltipp auf „Start“ kreuzt nichts an');
  lastNav = Date.now();
  const total = await p.evaluate(() => S.run.items.length);
  ok(total === 5, 'Quiz mit 5 Fragen');
  ok(await p.evaluate(() => { const idx = new Map(order().map((n,i) => [n,i])); const a = S.run.items.map(x => idx.get(x.p.n)); return a.every((v,i) => i === 0 || v >= a[i-1]); }), 'Reihenfolge nach Paragraf');
  ok(await p.locator('.lmini svg.tap').count() === 1, 'Lexi hüpft bei neuer Frage');
  for (let i = 0; i < total; i++) {
    await p.evaluate(() => { const it = S.run.items[S.run.i]; S.run.ticked = new Set(it.q.s.map((x, k) => x.w ? k : -1).filter(k => k >= 0)); });
    await p.click('[data-act="check"]'); await wait(500);
    await p.click('[data-act="next"]'); await wait(500);
  }
  await p.waitForSelector('.ring');
  const rt = await p.textContent('#app');
  ok(/von 20 Punkten/.test(rt) && rt.includes('Note 1') && rt.includes('100 %'), 'Ergebnis: Prozent, Maximum, Note 1');
  ok(await p.locator('svg.dance-hop').count() >= 1 && await p.locator('.conf i').count() === 18, 'Lexi tanzt (Hüpfen) mit Konfetti');
  await wait(900); ok(await p.locator('#sheet .dlg').count() === 1 && await p.locator('#sheet .dlg svg').count() === 1, 'Easter Egg mit Lexi');
  await p.click('#sheet .btn'); await wait(200);
  ok(!(await p.locator('#sheet .dlg').count()), 'Easter Egg schließbar');

  /* ---- Tutorial wiederholen, Abbrechen mit Spruch ---- */
  const histBefore = await p.evaluate(() => localStorage.getItem('rt.hist2'));
  await p.click('[data-act="home"]'); await p.click('[data-act="settings"]'); await p.click('[data-s="tour"]');
  ok(await p.locator('[data-act="tour-start"]').count() === 1, 'Tutorial aus den Einstellungen');
  // 10 Klicks reichen sicher zum Überspringen; hier lieber starten
  await p.click('[data-act="tour-start"]');
  for (let i = 0; i < 6; i++) {
    await wait(520);
    ok(await p.locator('.spot').count() === 1 && (await p.textContent('.tcard h3')).length > 3, 'Tutorial-Schritt ' + (i + 1) + ': ' + (await p.textContent('.tcard h3')));
    const sp = await p.evaluate(() => { const s = document.querySelector('.spot'); return parseFloat(s.style.width) > 20 && parseFloat(s.style.height) > 20; });
    ok(sp, '   Hervorhebung hat Größe');
    if (i === 2) await p.screenshot({ path: '/tmp/s_tour3.png' });
    if (i < 5) await p.click('[data-act="tour-next"]');
  }
  await wait(520); await p.click('[data-act="tour-next"]'); await wait(300);
  ok(await p.locator('.tcard').count() === 0 && await p.locator('.hero').count() === 1, 'Tour endet auf der Startseite');
  ok((await p.evaluate(() => localStorage.getItem('rt.hist2'))) === histBefore, 'Tour verändert keinen Lernfortschritt');
  await p.click('[data-act="to-start"]').catch(() => {});
  await p.evaluate(() => { document.querySelector('[data-act="settings"]').click(); }); await p.click('[data-s="tour"]'); await p.click('[data-act="tour-start"]'); await wait(300);
  await wait(520); await p.click('[data-act="tour-next"]'); await wait(520); await p.click('[data-act="tour-cancel"]'); await wait(300);
  ok((await p.textContent('#ovl')).includes('Keiner mag Klugscheißer.'), 'Abbrechen: Lexi sagt „Keiner mag Klugscheißer.“');
  await wait(3100); ok(await p.locator('.quipw').count() === 0, 'Spruch verschwindet');
  ok(await p.evaluate(() => S.run && S.run.res.length === 5), 'laufende Auswertung bleibt nach Tour erhalten');

  /* ---- Verweise (wie bisher) ---- */
  const ids = await p.evaluate(() => { const o = []; S.data.paragrafen.forEach(pp => pp.q.forEach(q => { if (q.s.some(s => REFRE && new RegExp(REFRE.source).test(esc(s.t)))) o.push(q.id); })); return o; });
  ok(ids.length >= 10, 'Fragen mit Verweisen: ' + ids.length);
  await p.evaluate(id => { const pool = []; S.data.paragrafen.forEach(pp => pp.q.forEach(q => { if (q.id === id) pool.push({ q, p: pp }); })); startRun(pool); }, ids[0]);
  await p.waitForSelector('.ref');
  const before = await p.evaluate(() => S.run.ticked.size);
  await p.click('.ref'); await p.waitForSelector('.pop');
  ok((await p.evaluate(() => S.run.ticked.size)) === before, 'Verweis antippen wählt Aussage nicht an');
  await p.keyboard.press('Escape'); await wait(150);
  ok(!(await p.isVisible('.pop')), 'Pop-up schließt mit Escape');

  /* ---- Weitere Prüfungen ---- */
  ok(await p.evaluate(() => /LexCoach/.test(SHARE_TEXT) && !/Rechtstrainer/.test(document.documentElement.outerHTML.replace(/localStorage[^;]*/g, ''))), 'kein „Rechtstrainer“ mehr im Seitenquelltext');
  const mf = JSON.parse(await (await fetch(URL + 'manifest.webmanifest')).text());
  ok(mf.name === 'LexCoach' && mf.short_name === 'LexCoach', 'Manifest: LexCoach');
  /* ---- Change-log nach Update (Wunsch 38) ---- */
  ok(await p.evaluate(() => localStorage.getItem('rt.seen') === '4'), 'neuer Nutzer: Change-log gilt als gesehen, kein Pop-up');
  const c2 = await b.newContext({ viewport: { width: 390, height: 780 } });
  await c2.addInitScript(() => { if (!sessionStorage.getItem('init')) { sessionStorage.setItem('init', '1'); localStorage.setItem('rt.tour', 'true'); localStorage.setItem('rt.a2hs', 'true'); } });
  const q = await c2.newPage(); q.setDefaultTimeout(6000);
  await q.goto(URL); await q.waitForSelector('#ovl .clg');
  ok((await q.textContent('#ovl')).includes('Neu in LexCoach') && (await q.textContent('#ovl')).includes('Sprechblase in der Kopfzeile') && !(await q.locator('#ovl svg').count()), 'bestehender Nutzer sieht das Change-log (ohne Lexi)');
  await q.click('[data-act="log-more"]'); ok((await q.textContent('#ovl')).includes('Change-log'), 'Frühere Updates klappen auf');
  await q.click('[data-act="log-close"]'); await wait(300);
  ok(await q.locator('#ovl').evaluate(e => e.innerHTML === '') && (await q.evaluate(() => localStorage.getItem('rt.seen'))) === '4', 'Alles klar schließt und merkt sich die Version');
  await q.reload(); await wait(800); ok(await q.locator('#ovl .clg').count() === 0, 'nach Neuladen kein Pop-up mehr');
  await q.click('[data-act="settings"]'); await q.click('[data-s="chg"]');
  ok((await q.textContent('#app')).includes('Change-log') && (await q.textContent('#app')).includes('Erste Version'), 'Einstellungen: Change-log zeigt alle Updates');
  ok(await q.locator('details.up').count() === 5 && await q.locator('details.up[open]').count() === 1, 'Change-log: 5 Updates, nur das neueste offen');
  await c2.close();
  /* ---- Karteikarten (Wunsch 41, versteckt hinter ?karten=1) ---- */
  const c3 = await b.newContext({ viewport: { width: 390, height: 780 } });
  await c3.addInitScript(() => { if (!sessionStorage.getItem('init')) { sessionStorage.setItem('init', '1'); localStorage.setItem('rt.tour', 'true'); localStorage.setItem('rt.a2hs', 'true'); localStorage.setItem('rt.seen', '4'); } });
  const k = await c3.newPage(); k.setDefaultTimeout(6000);
  await k.goto(URL); await k.waitForSelector('#app'); await wait(500);
  await k.click('[data-act="tab"][data-v="home"]'); await wait(600);
  ok(await k.locator('[data-act="mode-soon"]').count() === 1 && await k.locator('[data-act="mode"][data-m="k"]').count() === 0, 'Karteikarten ohne ?karten=1 gesperrt (Bald)');
  await k.goto(URL + '?karten=1'); await k.waitForSelector('#app'); await wait(500);
  await k.click('[data-act="tab"][data-v="home"]'); await wait(600);
  await k.click('[data-act="grp"][data-g="2"]'); await wait(300); await k.click('[data-act="tog"][data-p="43"]'); await wait(300); await k.click('[data-act="tog"][data-p="44"]'); await wait(300);
  const fN = async () => +((await k.textContent('.startbar')).match(/Start · (\d+) Fragen/) || [0, 0])[1];
  const nLM = await fN(); await k.click('[data-act="klv"][data-l="3"]'); await wait(300); const nAll = await fN();
  ok(nLM > 0 && nAll > nLM, 'Stufen: mit „schwer“ mehr Fragen (' + nLM + ' → ' + nAll + ')');
  await k.click('[data-act="klv"][data-l="3"]'); await wait(300); await k.click('[data-act="klv"][data-l="2"]'); await wait(300); const nL = await fN();
  ok(nL > 0 && nL < nLM, 'Stufen: nur „leicht“ ist weniger als „leicht + mittel“ (' + nL + ' < ' + nLM + ')');
  await k.click('[data-act="klv"][data-l="2"]'); await wait(300);
  await k.click('[data-act="mode"][data-m="k"]'); await wait(400);
  ok((await k.textContent('.startbar')).includes('Karten starten'), 'Kartenmodus: Startknopf zeigt Karten');
  await k.click('[data-act="kstart"]'); await wait(500);
  ok(await k.locator('#kflip').count() === 1 && !(await k.locator('#kflip').getAttribute('class')).includes('back'), 'Karte startet mit der Frage');
  await k.click('#dock [data-act="kflip"]'); await wait(300);
  ok((await k.locator('#kflip').getAttribute('class')).includes('back') && await k.locator('[data-act="kyes"]').count() === 1, 'Umdrehen zeigt Antwort und Bewertungsknöpfe');
  await k.click('[data-act="kno"]'); await wait(600);
  ok(await k.evaluate(() => Object.values(JSON.parse(localStorage.getItem('rt.cards') || '{}')).length === 1), 'Bewertung wird im Fach gespeichert');
  let kn = 0; while (await k.locator("#kflip").count() && kn++ < 30) { await k.click('#dock [data-act="kflip"]'); await wait(500); await k.click('[data-act="kyes"]'); await wait(600); }
  ok((await k.textContent('#app')).includes('Karten geschafft'), 'Kartendurchgang endet mit Zusammenfassung');
  await k.evaluate(() => { S.cr = {items:[{c:KARTEN.find(c => /§ 43 Abs\. 2/.test(c.q + c.a)) || KARTEN[0], retry:false}], i:0, back:false, yes:0, no:0}; S.view = 'cards'; render(); });
  await wait(300);
  const rf = k.locator('.kface .ref').first();
  if (await rf.count()) { await rf.click({ force: true }); await wait(400); ok((await k.textContent('#sheet')).includes('Abs.') && (await k.textContent('#sheet')).includes('Im RIS öffnen'), 'Verweis in Karte öffnet Pop-up mit Absatztext'); }
  else ok(false, 'Verweis in Karte vorhanden');
  await c3.close();
  ok(errs.length === 0, 'keine Konsolenfehler ' + errs.join(' | '));
  await b.close();
  console.log(fails ? fails + ' FEHLER' : 'ALLES OK');
  process.exit(fails ? 1 : 0);
})();
