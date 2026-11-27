#!/usr/bin/env python3
"""Wunsch 57: Export und Import des Lernstands (Einstellungen > Sicherung).
Nutzung: w57.py repo | w57.py vorschau <Ordner> (Repo bleibt unberuehrt)"""
import os, re, shutil, sys
SRC = '/home/user/lernapp'

CSS = '''.bkta{width:100%;min-height:96px;border:1.5px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink);font:12px/1.35 ui-monospace,Menlo,monospace;padding:10px;resize:vertical;word-break:break-all}
.bkbox{margin-bottom:12px}
.bkbox h3{font-size:15px;margin:0 0 4px}
.bkbox .mute{font-size:12.5px;margin-bottom:8px}
.bkrow{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.bkrow .btn{width:auto;flex:1;min-width:120px;padding:11px}
.bkwarn{background:var(--warn-bg);border:1.5px solid var(--warn);border-radius:12px;padding:10px 12px;margin-top:10px;font-size:13.5px}
.bkerr{color:var(--bad);font-size:13px;margin-top:6px}
.bkfile{display:block;margin-top:8px;font-size:13px}
'''

FUNCS = '''/* ---------- Sicherung (Wunsch 57): Lernstand als Textcode sichern und laden ---------- */
function bkMake(){
  const d = {};
  for(let i = 0; i < localStorage.length; i++){ const k = localStorage.key(i); if(k && k.startsWith('rt.') && k !== 'rt.bk') d[k] = localStorage.getItem(k); }
  const j = JSON.stringify({app:'lexcoach', v:1, t:Date.now(), d});
  return 'LEXCOACH1:' + btoa(unescape(encodeURIComponent(j)));
}
function bkRead(txt){
  const m = /LEXCOACH1:([A-Za-z0-9+\\/=\\s]+)/.exec(txt || '');
  if(!m) throw new Error('format');
  const j = JSON.parse(decodeURIComponent(escape(atob(m[1].replace(/\\s+/g, '')))));
  if(!j || j.app !== 'lexcoach' || !j.d || typeof j.d !== 'object') throw new Error('app');
  return j;
}
const bkDate = t => new Date(t).toLocaleDateString('de-AT', {day:'2-digit', month:'2-digit', year:'numeric'});
function bkSummary(j){
  let n = 0, k = 0;
  try{ n = Object.keys(JSON.parse(j.d['rt.hist2'] || '{}')).length; }catch(e){}
  try{ k = (JSON.parse(j.d['rt.klausur'] || '[]') || []).length; }catch(e){}
  return `Sicherung vom ${bkDate(j.t)}: ${n} Fragen mit Fortschritt, ${k} Klausur${k === 1 ? '' : 'en'} in der Historie.`;
}
'''

PAGE = '''  } else if(S.set === 'backup'){
    const last = store.get('rt.bk', 0);
    h = back('Einstellungen') + `<div class="top"><h1>Sicherung</h1></div>
      <p class="hint" style="margin-top:0">Dein Lernstand liegt nur auf diesem Gerät. Mit einer Sicherung nimmst du ihn auf ein neues Gerät mit, auch zwischen Safari und der Home-Bildschirm-App.</p>
      <div class="card bkbox"><h3>Sicherung erstellen</h3><div class="mute" id="bklast">${last ? 'Letzte Sicherung: ' + bkDate(last) : 'Noch keine Sicherung erstellt.'}</div>
        <button class="btn" data-act="bk-make">Sicherung erstellen</button>
        <div id="bkres" hidden><textarea class="bkta" id="bkout" readonly aria-label="Sicherungstext"></textarea>
          <div class="bkrow"><button class="btn alt" data-act="bk-copy">Text kopieren</button><button class="btn alt" id="bkshare" data-act="bk-share" hidden>Teilen</button></div>
          <p class="hint">Füge den Text in eine Notiz oder Nachricht an dich selbst ein, oder teile ihn.</p></div></div>
      <div class="card bkbox"><h3>Sicherung laden</h3><div class="mute">Text einfügen oder Datei wählen.</div>
        <textarea class="bkta" id="bkin" placeholder="Sicherungstext hier einfügen" aria-label="Sicherungstext einfügen"></textarea>
        <label class="bkfile">Oder Datei wählen: <input type="file" id="bkfile" accept=".txt,text/plain"></label>
        <div class="bkerr" id="bkerr" role="alert"></div>
        <div class="bkrow"><button class="btn alt" data-act="bk-ask">Laden</button></div>
        <div class="bkwarn" id="bkask" hidden><b id="bksum"></b><br>Das ersetzt deinen jetzigen Lernstand auf diesem Gerät. Fortfahren?
          <div class="bkrow"><button class="btn" data-act="bk-yes">Ja, ersetzen</button><button class="btn alt" data-act="bk-no">Abbrechen</button></div></div></div>`;
'''

ACTS = '''  'bk-make'(){ const c = bkMake(); $('#bkout').value = c; $('#bkres').hidden = false; store.set('rt.bk', Date.now()); const l = $('#bklast'); if(l) l.textContent = 'Letzte Sicherung: ' + bkDate(Date.now()); const sh = $('#bkshare'); if(sh) sh.hidden = !navigator.share; },
  'bk-copy'(){ const o = $('#bkout'); o.focus(); o.select(); try{ navigator.clipboard.writeText(o.value).then(() => toast('Kopiert'), () => { document.execCommand('copy'); toast('Kopiert'); }); }catch(e){ try{ document.execCommand('copy'); toast('Kopiert'); }catch(e2){} } },
  'bk-share'(){ const c = $('#bkout').value; try{ const f = new File([c], 'lexcoach-sicherung.txt', {type:'text/plain'}); if(navigator.canShare && navigator.canShare({files:[f]})) navigator.share({files:[f], title:'LexCoach Sicherung'}).catch(() => {}); else navigator.share({text:c, title:'LexCoach Sicherung'}).catch(() => {}); }catch(e){} },
  'bk-ask'(){ const err = $('#bkerr'); err.textContent = ''; $('#bkask').hidden = true; try{ const j = bkRead($('#bkin').value); S.bkpend = j; $('#bksum').textContent = bkSummary(j); $('#bkask').hidden = false; }catch(e){ S.bkpend = null; err.textContent = 'Das ist keine gültige LexCoach-Sicherung. Bitte den ganzen Text einfügen, er beginnt mit LEXCOACH1:.'; } },
  'bk-no'(){ S.bkpend = null; $('#bkask').hidden = true; },
  'bk-yes'(){ const j = S.bkpend; if(!j) return; const del = []; for(let i = 0; i < localStorage.length; i++){ const k = localStorage.key(i); if(k && k.startsWith('rt.')) del.push(k); } del.forEach(k => localStorage.removeItem(k)); Object.keys(j.d).forEach(k => { if(k.startsWith('rt.') && typeof j.d[k] === 'string') localStorage.setItem(k, j.d[k]); }); try{ sessionStorage.setItem('bkdone', '1'); }catch(e){} location.reload(); },
'''

def patch(s):
    def rep(a, b):
        nonlocal s
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    rep("function toast(msg){", FUNCS + "function toast(msg){")
    rep("      + row('legal', '§', 'Rechtliches',", "      + row('backup', '⇅', 'Sicherung', store.get('rt.bk', 0) ? 'Letzte Sicherung: ' + bkDate(store.get('rt.bk', 0)) : 'Lernstand sichern und laden')\n      + row('legal', '§', 'Rechtliches',")
    rep("  } else if(S.set === 'legal'){", PAGE + "  } else if(S.set === 'legal'){")
    rep("  'set-ord'(b){", ACTS + "  'set-ord'(b){")
    rep(".stack2{display:grid;gap:8px}", ".stack2{display:grid;gap:8px}\n" + CSS.rstrip('\n'))
    rep("document.addEventListener('input', e => {", """document.addEventListener('change', e => {
  const t = e.target;
  if(t.id === 'bkfile' && t.files && t.files[0]){ const r = new FileReader(); r.onload = () => { const a = $('#bkin'); if(a) a.value = String(r.result || ''); }; r.readAsText(t.files[0]); }
});
document.addEventListener('input', e => {""")
    # nach dem Laden Hinweis
    rep("  render();\n})();\nif('serviceWorker'", "  render();\n  try{ if(sessionStorage.getItem('bkdone')){ sessionStorage.removeItem('bkdone'); setTimeout(() => toast('Sicherung geladen'), 400); } }catch(e){}\n})();\nif('serviceWorker'")
    # Zurueck-Pfeil: Unterseite 'backup' fuehrt ins Menue (Standard: menu) -> nichts zu tun
    return s

if __name__ == '__main__':
    mode = sys.argv[1]
    s = patch(open(os.path.join(SRC, 'index.html'), encoding='utf-8').read())
    if mode == 'repo':
        open(os.path.join(SRC, 'index.html'), 'w', encoding='utf-8').write(s)
        print('repo ok')
    else:
        OUT = sys.argv[2]
        os.makedirs(OUT, exist_ok=True)
        for f in ['lexi.js', 'lexi.css', 'legal.js']:
            shutil.copy(os.path.join(SRC, f), OUT)
        for d in ['daten', 'fonts', 'vendor']:
            shutil.copytree(os.path.join(SRC, d), os.path.join(OUT, d), dirs_exist_ok=True)
        boot = '''<script>
try{ localStorage.setItem('rt.tour','true'); localStorage.setItem('rt.a2hs','true'); localStorage.setItem('rt.seen','99'); }catch(e){}
window.PREVIEW_BOOT = function(){
  try{
    if(!localStorage.getItem('rt.hist2')){
      const h = {}; S.data.paragrafen.slice(0, 6).forEach(p => p.q.slice(0, 5).forEach(q => { h[q.id] = {last: 3 + (q.id.length % 2), n: 1}; }));
      localStorage.setItem('rt.hist2', JSON.stringify(h));
      localStorage.setItem('rt.klausur', JSON.stringify([{id:'a',t:Date.now()-86400000,name:'Beispiel',law:'BDG',paras:['4'],n:5,pts:17,mx:20,pc:85,note:2}]));
    }
    S.prev = 'start'; S.view = 'settings'; S.set = 'backup'; render();
  }catch(e){}
};
</script>
'''
        a = '<script src="vendor/qrcode.js"></script>'
        assert s.count(a) == 1
        s = s.replace(a, boot + a)
        a = "  render();\n  try{ if(sessionStorage"
        assert s.count(a) == 1
        s = s.replace(a, "  render(); if(window.PREVIEW_BOOT && !sessionStorage.getItem('bkdone')) window.PREVIEW_BOOT();\n  try{ if(sessionStorage")
        open(os.path.join(OUT, 'index_full.html'), 'w', encoding='utf-8').write(s)
        lexi = open(os.path.join(SRC, 'lexi.css'), encoding='utf-8').read()
        style = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
        body = s[s.index('<body>') + 6:s.index('</body>')]
        open(os.path.join(OUT, 'vorschau.html'), 'w', encoding='utf-8').write('<title>LexCoach Vorschau</title>\n<style>' + lexi + '</style>\n<style>' + style + '</style>\n' + body)
        print('vorschau ok')
