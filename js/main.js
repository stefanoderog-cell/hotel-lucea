/* Hotel Lucea — interazioni (vanilla JS, nessuna dipendenza) */
(function () {
  'use strict';
  var C = window.LUCEA_CONFIG || {};
  var I = window.LUCEA_I18N || { en: {}, dyn: { it: {}, en: {} } };
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var has = function (v) { return typeof v === 'string' && v.trim() !== ''; };
  var lang = root.lang === 'en' ? 'en' : 'it';
  var D = function (k) { return (I.dyn[lang] && I.dyn[lang][k]) || I.dyn.it[k] || k; };

  /* ---------- i18n ---------- */
  var META = {
    it: { title: document.title, desc: $('meta[name=description]').content },
    en: { title: 'Hotel Lucea · Naples — Where Naples lights up', desc: 'Hotel Lucea in Naples: bright rooms, Neapolitan hospitality and Vesuvius on the horizon. Where Naples lights up. Book directly via WhatsApp or email.' }
  };
  var itCache = new Map();
  $$('[data-i18n]').forEach(function (el) { itCache.set(el, el.innerHTML); });
  var attrCache = new Map();
  $$('[data-i18n-attr]').forEach(function (el) {
    var o = {};
    el.getAttribute('data-i18n-attr').split(';').forEach(function (p) { var a = p.split(':')[0]; o[a] = el.getAttribute(a); });
    attrCache.set(el, o);
  });
  function applyLang(l) {
    lang = l; root.lang = l;
    itCache.forEach(function (it, el) {
      var k = el.getAttribute('data-i18n');
      el.innerHTML = (l === 'en' && I.en[k] != null) ? I.en[k] : it;
    });
    attrCache.forEach(function (orig, el) {
      el.getAttribute('data-i18n-attr').split(';').forEach(function (p) {
        var a = p.split(':')[0], k = p.split(':')[1];
        el.setAttribute(a, (l === 'en' && I.en[k] != null) ? I.en[k] : orig[a]);
      });
    });
    document.title = META[l].title;
    $('meta[name=description]').content = META[l].desc;
    $$('.lang button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.lang === l)); });
    try { localStorage.setItem('lucea-lang', l); } catch (e) {}
    renderContacts(); updateNights(); setupLinks();
  }
  $$('.lang button').forEach(function (b) { b.addEventListener('click', function () { applyLang(b.dataset.lang); }); });

  /* ---------- tema chiaro/scuro ---------- */
  $('.theme-btn').addEventListener('click', function () {
    var cur = root.dataset.theme;
    var dark = cur === 'dark' || (cur === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('lucea-theme', root.dataset.theme); } catch (e) {}
  });

  /* ---------- menu mobile ---------- */
  var menuBtn = $('.menu-btn'), nav = $('#nav');
  function closeMenu() { nav.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); }
  menuBtn.addEventListener('click', function () {
    var open = !nav.classList.contains('open');
    nav.classList.toggle('open', open); menuBtn.setAttribute('aria-expanded', String(open));
    if (open) { var a = $('a', nav); a && a.focus(); }
  });
  $$('a', nav).forEach(function (a) { a.addEventListener('click', closeMenu); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { closeMenu(); menuBtn.focus(); } });

  /* ---------- luci della città (hero) ---------- */
  var g = $('#city-lights');
  if (g) {
    var NS = 'http://www.w3.org/2000/svg', seed = 11;
    var rnd = function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
    var frag = document.createDocumentFragment();
    for (var i = 0; i < 190; i++) {
      var c = document.createElementNS(NS, 'circle');
      var x = rnd() * 1840 - 200, y;
      // costa e paesi vesuviani (sotto il profilo dei monti, sopra il mare)
      // altezza disponibile sotto il profilo dei monti (più alta verso il centro)
      var hmax = Math.max(5, 58 * (1 - Math.abs(x - 720) / 520));
      y = 768 - rnd() * hmax;
      c.setAttribute('cx', x.toFixed(1)); c.setAttribute('cy', y.toFixed(1));
      c.setAttribute('r', (0.9 + rnd() * 1.9).toFixed(2));
      c.setAttribute('fill', rnd() > .25 ? '#FFD27A' : '#FFF1CF');
      c.style.setProperty('--d', (rnd() * 1.3).toFixed(2));
      if (rnd() > .7) c.setAttribute('class', 'tw');
      c.style.animationDelay = (-rnd() * 3).toFixed(2) + 's';
      frag.appendChild(c);
    }
    // riflessi delle luci sul mare
    for (var j = 0; j < 45; j++) {
      var r = document.createElementNS(NS, 'rect');
      r.setAttribute('x', (rnd() * 1840 - 200).toFixed(0)); r.setAttribute('y', (780 + rnd() * 115).toFixed(0));
      r.setAttribute('width', (8 + rnd() * 30).toFixed(0)); r.setAttribute('height', '2'); r.setAttribute('rx', '1');
      r.setAttribute('fill', '#FFD27A'); r.setAttribute('opacity', (.25 + rnd() * .4).toFixed(2));
      r.style.setProperty('--d', (.4 + rnd()).toFixed(2));
      frag.appendChild(r);
    }
    g.appendChild(frag);
    var css = document.createElement('style');
    css.textContent = '.city-lights rect{opacity:clamp(0,calc(var(--p)*2.4 - var(--d)),.6)}';
    document.head.appendChild(css);
  }

  /* ---------- inquadratura hero su schermi verticali ---------- */
  var art = $('.hero-art');
  function frameHero() {
    if (!art) return;
    var portrait = window.innerWidth / window.innerHeight < 0.9;
    art.setAttribute('viewBox', portrait ? '380 470 680 480' : '0 0 1440 900');
    art.setAttribute('preserveAspectRatio', portrait ? 'xMidYMax meet' : 'xMidYMax slice');
  }
  frameHero();
  window.addEventListener('resize', frameHero, { passive: true });

  /* ---------- "si accende": progresso di scroll ---------- */
  var hero = $('#hero'), header = $('.site-header'), ticking = false;
  function onScroll() {
    var y = window.scrollY, vh = window.innerHeight;
    var hp = Math.min(1, Math.max(0, y / Math.max(1, hero.offsetHeight - vh)));
    var gp = Math.min(1, Math.max(0, y / (document.documentElement.scrollHeight - vh)));
    root.style.setProperty('--p', hp.toFixed(3));
    root.style.setProperty('--g', gp.toFixed(3));
    header.classList.toggle('solid', y > hero.offsetHeight - 80);
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* ---------- reveal & sezione attiva ---------- */
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); } });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    $$('.reveal, .lit, .nap').forEach(function (el) { io.observe(el); });
  } else {
    $$('.reveal, .lit, .nap').forEach(function (el) { el.classList.add('on'); });
  }
  if ('IntersectionObserver' in window) {
    var links = $$('.nav a');
    var spy = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) links.forEach(function (a) { a.setAttribute('aria-current', String(a.getAttribute('href') === '#' + e.target.id)); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    $$('main section[id]').forEach(function (s) { spy.observe(s); });
  }

  /* ---------- luce che segue il puntatore sulle card ---------- */
  if (!reduce && window.matchMedia('(hover: hover)').matches) {
    document.addEventListener('pointermove', function (e) {
      var card = e.target.closest && e.target.closest('.glow-card');
      if (!card) return;
      var r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      card.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }, { passive: true });
  }

  /* ---------- contatti da config ---------- */
  function digits(s) { return (s || '').replace(/[^\d+]/g, ''); }
  function waNumber() { return (C.whatsapp || '').replace(/\D/g, ''); }
  function todo() { return '<span class="todo">' + D('todo') + '</span>'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function renderContacts() {
    var a = C.indirizzo || {};
    var addr = [a.via, [a.cap, a.citta, a.provincia ? '(' + a.provincia + ')' : ''].filter(Boolean).join(' ')].filter(has).join(', ');
    var map = {
      email: has(C.email) ? '<a href="mailto:' + esc(C.email) + '">' + esc(C.email) + '</a>' : todo(),
      tel: has(C.tel) ? '<a href="tel:' + esc(digits(C.tel)) + '">' + esc(C.tel) + '</a>' : todo(),
      web: has(C.web) ? '<a href="' + esc(C.web) + '">' + esc(C.web.replace(/^https?:\/\//, '')) + '</a>' : todo(),
      cell: has(C.cell) ? '<a href="tel:' + esc(digits(C.cell)) + '">' + esc(C.cell) + '</a>' : todo(),
      whatsapp: waNumber() ? '<a href="https://wa.me/' + waNumber() + '" target="_blank" rel="noopener">+' + waNumber() + '</a>' : todo(),
      indirizzo: has(a.via) ? esc(addr) : todo(),
      cin: has(C.cin) ? esc(C.cin) : todo(),
      piva: has(C.piva) ? esc(C.piva) : todo()
    };
    $$('[data-contact]').forEach(function (el) { el.innerHTML = map[el.dataset.contact] || todo(); });
  }

  function setupLinks() {
    var wa = $('#wa-float'), n = waNumber();
    if (n) { wa.href = 'https://wa.me/' + n; wa.target = '_blank'; wa.rel = 'noopener'; }
    var mel = $('#melodia-link');
    if (has(C.melodiaUrl)) { mel.href = C.melodiaUrl; mel.target = '_blank'; mel.rel = 'noopener'; mel.removeAttribute('aria-disabled'); }
    else { mel.setAttribute('aria-disabled', 'true'); mel.removeAttribute('href'); mel.title = D('soon'); }
    var be = $('#booking-engine-link');
    if (has(C.bookingEngineUrl)) { be.href = C.bookingEngineUrl; be.hidden = false; }
    var pv = $('#privacy-link');
    if (has(C.privacyUrl)) pv.href = C.privacyUrl; else pv.removeAttribute('href');
  }

  // mappa
  if (has(C.mappaEmbedUrl)) {
    var m = $('#map');
    m.innerHTML = '<iframe title="Mappa Hotel Lucea" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen src="' + esc(C.mappaEmbedUrl) + '"></iframe>';
  }

  // SEO: dati strutturati e canonical da config
  (function seo() {
    var el = $('#jsonld'); if (!el) return;
    try {
      var j = JSON.parse(el.textContent), a = C.indirizzo || {};
      if (has(a.via)) j.address.streetAddress = a.via;
      if (has(a.cap)) j.address.postalCode = a.cap;
      if (has(a.citta)) j.address.addressLocality = a.citta;
      if (has(C.tel || C.cell)) j.telephone = C.tel || C.cell;
      if (has(C.email)) j.email = C.email;
      if (has(C.web)) { j.url = C.web; $('link[rel=canonical]').href = C.web; }
      j.sameAs = [C.instagram, C.facebook].filter(has);
      el.textContent = JSON.stringify(j);
    } catch (e) {}
  })();

  /* ---------- prenotazione ---------- */
  var f = $('#book-form'), fin = $('#f-in'), fout = $('#f-out'), err = $('#form-error'), nightsEl = $('#nights');
  function iso(d) { return new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString().slice(0, 10); }
  var today = new Date(); today.setHours(0, 0, 0, 0);
  fin.min = iso(today);
  fout.min = iso(new Date(today.getTime() + 864e5));
  function nights() {
    if (!fin.value || !fout.value) return 0;
    return Math.round((new Date(fout.value) - new Date(fin.value)) / 864e5);
  }
  function updateNights() {
    var n = nights();
    nightsEl.textContent = n > 0 ? (n === 1 ? D('nights1') : D('nightsN').replace('{n}', n)) : '';
  }
  fin.addEventListener('change', function () {
    if (fin.value) {
      var next = new Date(fin.value); next.setDate(next.getDate() + 1);
      fout.min = iso(next);
      if (!fout.value || fout.value <= fin.value) fout.value = iso(next);
    }
    updateNights(); err.textContent = ''; fin.removeAttribute('aria-invalid');
  });
  fout.addEventListener('change', function () { updateNights(); err.textContent = ''; fout.removeAttribute('aria-invalid'); });
  $$('.stepper').forEach(function (s) {
    var inp = $('input', s);
    $$('button', s).forEach(function (b) {
      b.addEventListener('click', function () {
        var v = (parseInt(inp.value, 10) || 0) + parseInt(b.dataset.step, 10);
        inp.value = Math.min(+inp.max, Math.max(+inp.min, v));
      });
    });
  });
  $$('[data-room]').forEach(function (a) {
    a.addEventListener('click', function () { $('#f-room').selectedIndex = +a.dataset.room; });
  });
  function fmt(v) { if (!v) return ''; var p = v.split('-'); return p[2] + '/' + p[1] + '/' + p[0]; }
  function message() {
    var room = $('#f-room'), lines = [D('msgHello'), '',
      '• ' + D('msgIn') + ': ' + fmt(fin.value),
      '• ' + D('msgOut') + ': ' + fmt(fout.value),
      '• ' + D('msgNights') + ': ' + nights(),
      '• ' + D('msgAdults') + ': ' + $('#f-ad').value,
      '• ' + D('msgChildren') + ': ' + $('#f-ch').value];
    if (room.selectedIndex > 0) lines.push('• ' + D('msgRoom') + ': ' + room.options[room.selectedIndex].text);
    if ($('#f-name').value.trim()) lines.push('• ' + D('msgName') + ': ' + $('#f-name').value.trim());
    if ($('#f-notes').value.trim()) lines.push('• ' + D('msgNotes') + ': ' + $('#f-notes').value.trim());
    lines.push('', D('msgThanks'));
    return lines.join('\n');
  }
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var via = (e.submitter && e.submitter.dataset.send) || 'wa';
    if (!fin.value || !fout.value || nights() < 1) {
      err.textContent = D('errDates');
      (!fin.value ? fin : fout).setAttribute('aria-invalid', 'true');
      (!fin.value ? fin : fout).focus();
      return;
    }
    var text = message();
    if (via === 'wa') {
      if (!waNumber()) { err.textContent = D('errNoWa'); return; }
      window.open('https://wa.me/' + waNumber() + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
    } else {
      if (!has(C.email)) { err.textContent = D('errNoMail'); return; }
      location.href = 'mailto:' + C.email + '?subject=' + encodeURIComponent(D('mailSubject') + ' — Hotel Lucea') + '&body=' + encodeURIComponent(text);
    }
    err.textContent = '';
  });

  $('#year').textContent = new Date().getFullYear();

  /* ---------- avvio ---------- */
  var q = new URLSearchParams(location.search).get('lang');
  applyLang(q === 'en' || q === 'it' ? q : lang);

  /* ---------- PWA: service worker (solo su http/https) ---------- */
  if ('serviceWorker' in navigator && /^https?:$/.test(location.protocol)) {
    window.addEventListener('load', function () { navigator.serviceWorker.register('sw.js').catch(function () {}); });
  }
})();
