#!/usr/bin/env python3
"""Baut aus dem Repo eine Vorschau-Kopie der echten App mit Wunsch 54 (nur Kopie, Repo bleibt unberuehrt)."""
import re, shutil, sys, os
SRC = '/home/user/lernapp'
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
for f in ['lexi.js', 'lexi.css', 'legal.js', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png']:
    shutil.copy(os.path.join(SRC, f), OUT)
for d in ['daten', 'fonts', 'vendor']:
    shutil.copytree(os.path.join(SRC, d), os.path.join(OUT, d), dirs_exist_ok=True)

s = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# ---- CSS: schlank, neutral, Kasten faerben, Frage-Kasten festhalten ----
i = s.index('.shead,.st{display:flex')
j = s.index('.cb.wrong[aria-pressed="true"] i{') ; j = s.index('\n', j) + 1
css = '''.qstick{position:sticky;top:env(safe-area-inset-top,0px);z-index:6;background:var(--bg);padding-top:8px;margin-top:-8px}
.qstick .qbox{margin-bottom:8px}
.shead,.st{display:flex;align-items:center;gap:0}
.shead{justify-content:flex-end;font-size:10px;font-weight:700;letter-spacing:0;text-transform:uppercase;color:var(--mute);margin:0;padding:0 2px 3px 0;border-bottom:1px solid var(--line)}
.shead span,.cb{width:50px;flex:none;text-align:center}
.shead .sp{flex:1;width:auto}
.st{border-bottom:1px solid var(--line);padding:9px 0 9px 8px;border-radius:8px}
.st .txt{flex:1;min-width:0;padding-right:8px;font-size:15px;line-height:1.4}
.cb{height:42px;display:grid;place-items:center;background:none;border:0;padding:0;cursor:pointer}
.cb i{display:grid;place-items:center;width:22px;height:22px;border-radius:5px;border:1.5px solid var(--mute);background:transparent;font-style:normal;font-weight:700;font-size:14px;line-height:1;color:var(--ink)}
.cb[aria-pressed="true"] i{border-color:var(--ink)}
.cb:focus-visible{outline:3px solid var(--acc);outline-offset:-4px;border-radius:8px}
.cb.sol i{border-color:var(--ink);border-width:2.5px}
.st.ok{background:color-mix(in srgb,var(--ok) 11%,transparent)}
.st.bad{background:color-mix(in srgb,var(--bad) 11%,transparent)}
.st.miss{background:color-mix(in srgb,var(--warn) 11%,transparent)}
.st .why{display:block;margin-top:5px;font-size:13px;color:var(--mute)}
.qhint{font-size:12.5px;color:var(--mute);margin:0 2px 10px}
'''
s = s[:i] + css + s[j:]

# ---- renderQ ----
a = s.index('    <div class="qbox"><div class="lab">')
b = s.index('`;', a) + 2
old = s[a:b]
m = re.search(r'<div class="hint">(.*?)</div></div>`;', old, re.S)
hint = m.group(1)
new = old.replace('<div class="hint">' + hint + '</div></div>`;', '</div>`;')
new = new.replace('    <div class="qbox">', '    <div class="qhint">' + hint + '</div>\n    <div class="qstick"><div class="qbox">', 1)
new = new.replace('</div>`;', '</div>`;', 1)
s = s[:a] + new + s[b:]
rep('''  h += `<div class="shead"><span class="sp"></span><span>Richtig</span><span>Falsch</span></div>`;''',
    '''  h += `<div class="shead"><span class="sp"></span><span>Richtig</span><span>Falsch</span></div></div>`;''')
# Info-Zeile entfaellt, Erklaerung bleibt
a = s.index("      const lab = pts > 0 ? '+1'")
b = s.index("    }\n    h += `<div class=\"st${cls}\">", a)
s = s[:a] + "      fb = (!s.w && s.k) ? `<span class=\"why\"><b>Erklärung:</b> ${esc(s.k)}</span>` : '';\n" + s[b:]

rep('html,body{margin:0;overflow-x:hidden;', 'html,body{margin:0;overflow-x:clip;')   # damit position:sticky greift

# ---- Vorschau-Start in die Frage ----
rep('  render();\n})();\nif(\'serviceWorker\'', '  render(); if(window.PREVIEW_BOOT) window.PREVIEW_BOOT();\n})();\nif(\'serviceWorker\'')
boot = '''<script>
try{ localStorage.setItem('rt.tour','true'); localStorage.setItem('rt.a2hs','true'); localStorage.setItem('rt.seen','99'); }catch(e){}
window.PREVIEW_BOOT = function(){
  try{
    const pp = S.data.paragrafen.find(x => x.n === '4') || S.data.paragrafen[0];
    const qs = pp.q.filter(q => !q.x && q.s.length === 4).slice(0, 3).map(q => ({q, p:pp}));
    S.view = 'home'; startRun(qs);
  }catch(e){}
};
</script>
'''
rep('<script src="vendor/qrcode.js"></script>', boot + '<script src="vendor/qrcode.js"></script>')

open(os.path.join(OUT, 'index_full.html'), 'w', encoding='utf-8').write(s)

# ---- Seite fuer das Artefakt (ohne Dokument-Huelle) ----
lexi = open(os.path.join(SRC, 'lexi.css'), encoding='utf-8').read()
style = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
body = s[s.index('<body>') + 6:s.index('</body>')]
page = '<title>LexCoach Vorschau</title>\n<style>' + lexi + '</style>\n<style>' + style + '</style>\n' + body
open(os.path.join(OUT, 'vorschau.html'), 'w', encoding='utf-8').write(page)
print('ok', len(page))
