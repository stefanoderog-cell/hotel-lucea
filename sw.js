/* Service worker minimale: cache offline delle risorse principali */
const CACHE = 'lucea-v1';
const ASSETS = ['./', 'index.html', 'css/style.css', 'js/config.js', 'js/i18n.js', 'js/main.js',
  'fonts/CormorantGaramond-SemiBold.woff2', 'fonts/CormorantGaramond-MediumItalic.woff2',
  'fonts/Montserrat-Light.woff2', 'fonts/Montserrat-Medium.woff2', 'img/favicon.svg', 'img/icon-192.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
/* network-first: i contenuti aggiornati (es. config.js) arrivano subito; offline usa la cache */
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(r => { const cp = r.clone(); caches.open(CACHE).then(c => c.put(e.request, cp)); return r; }).catch(() => caches.match(e.request)));
});
