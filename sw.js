// Offline-Cache für LexCoach.
// Strategie: erst Netz (max. 3 s), sonst Cache -> Änderungen sind sofort beim nächsten Öffnen da, Offline funktioniert trotzdem.
// Bei neuen Dateien oder umbenannten Pfaden VERSION erhöhen.
const VERSION = 'rt-v13';
const ASSETS = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png', 'daten/bdg.json', 'daten/verweise.json', 'daten/news.json', 'daten/changelog.json', 'lexi.js', 'lexi.css', 'legal.js', 'vendor/qrcode.js'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith('rt-') && k !== VERSION).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  e.respondWith(caches.open(VERSION).then(cache => {
    const fromCache = () => cache.match(req, {ignoreSearch: true});
    // Fehlerantworten (404, 503 …) dürfen eine gute Kopie im Cache nicht verdrängen.
    const net = fetch(req, {cache: 'no-cache'}).then(res => {
      if (res.ok) { cache.put(req, res.clone()).catch(() => {}); return res; }
      return fromCache().then(hit => hit || res);
    });
    net.catch(() => {});
    const timeout = new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), 3000));
    return Promise.race([net, timeout]).catch(() => fromCache().then(hit => hit || net));
  }));
});
