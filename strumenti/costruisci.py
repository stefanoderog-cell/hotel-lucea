#!/usr/bin/env python3
"""Assembla index.html da index.template.html (blocchi ripetuti: camere, servizi, Napoli, galleria).
Uso: python3 strumenti/costruisci.py   (dalla cartella del sito)"""
import os, random
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PROF = "M315.0,296 C375.0,292 435.0,256 476.0,242 C494.0,235 512.0,235 526.0,244 C542.0,252 560.0,256 580.0,256 C600.0,256 622.0,234 636.0,218 L641.0,213 L677.0,213 L682.0,218 C702.0,240 750.0,274 805.0,287 C838.0,294 862.0,296 885.0,296"
RAYS = '<path d="M517.98,229.43 L476.63,214.38"/><path d="M524.52,216.25 L504.35,203.25"/><path d="M533.82,204.84 L503.04,173.41"/><path d="M545.42,195.79 L532.84,175.34"/><path d="M558.73,189.52 L544.55,147.87"/><path d="M573.1,186.36 L570.59,162.49"/><path d="M587.81,186.46 L593.02,142.77"/><path d="M602.14,189.82 L610.19,167.21"/><path d="M615.36,196.27 L638.94,159.12"/><path d="M626.83,205.49 L643.86,188.58"/>'

LOGO = f'''<svg class="logo" viewBox="410 128 380 180" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round" class="logo-rays">{RAYS}</g><path d="M528,252 A52,52 0 0 1 632,252 L632,298 L528,298 Z" class="logo-sun" clip-path="url(#logo-clip)"/><path d="{PROF}" fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

WA = '<svg class="wa-ico" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path fill="currentColor" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 6.9L3.2 29l6.5-1.7c1.9 1 4.1 1.6 6.3 1.6 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.5c-2 0-4-.5-5.6-1.5l-.4-.2-3.9 1 1-3.8-.3-.4c-1.1-1.7-1.7-3.7-1.7-5.8C5.1 9.9 10 5.1 16 5.1s10.9 4.8 10.9 10.7S22 26.5 16 26.5zm6-8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.3 1.4.5 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'

ROOMS = [
 ('room1','camera-classica','Camera Classica','Calda e raccolta, con arredi in legno, lino chiaro e dettagli in ottone: il rifugio ideale dopo una giornata in città.'),
 ('room2','camera-superior','Superior Vista','Più spazio e più luce, pensata per chi ama aprire le finestre e lasciarsi sorprendere da Napoli.'),
 ('room3','camera-junior','Junior Suite','Un piccolo salotto, materiali pregiati e un’atmosfera che si accende al calar della sera.'),
 ('room4','camera-familiare','Camera Familiare','Spazi pensati per viaggiare insieme, con il comfort di una casa napoletana.'),
]
rooms=''
for i,(k,img,name,desc) in enumerate(ROOMS):
    rooms += f'''<article class="room glow-card reveal" style="--i:{i}">
        <div class="room-media"><img src="img/{img}.svg" alt="" width="1200" height="800" loading="lazy" decoding="async"><span class="photo-badge" data-i18n="photoBadge">Foto reale in arrivo</span></div>
        <div class="room-body">
          <h3 data-i18n="{k}.name">{name}</h3>
          <p data-i18n="{k}.desc">{desc}</p>
          <ul class="room-facts" role="list"><li><span data-i18n="rooms.guests">Ospiti</span> —</li><li><span data-i18n="rooms.size">Superficie</span> — m²</li><li><span data-i18n="rooms.view">Vista</span> —</li></ul>
          <div class="room-foot"><p class="price"><span class="price-val">€ —</span> <span class="price-unit" data-i18n="rooms.night">a notte · tariffa da definire</span></p>
          <a class="btn btn-sm btn-ghost-dark" href="#prenota" data-room="{i+1}" data-i18n="rooms.cta">Verifica disponibilità</a></div>
        </div>
      </article>
      '''

IC = {
 'wifi':'<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1"/>',
 'coffee':'<path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM17 10h1.5a2.5 2.5 0 0 1 0 5H17M8 2.5c-.8 1 .8 2 0 3M12 2.5c-.8 1 .8 2 0 3"/>',
 'snow':'<path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7M9 4l3 2 3-2M9 20l3-2 3 2"/>',
 'bell':'<path d="M4 18h16M6 18a6 6 0 0 1 12 0M12 12V10M10 9.5h4M2.5 21h19"/>',
 'bag':'<rect x="4" y="7" width="16" height="13" rx="2"/><path d="M9 7V4h6v3M9 11v5M15 11v5"/>',
 'map':'<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2zM9 4v14M15 6v14"/>',
 'car':'<path d="M3 16v-4l2.5-5h13L21 12v4zM3 16v2h3v-2M18 16v2h3v-2M6.5 13h.01M17.5 13h.01"/>',
 'spark':'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>',
}
SERV = [('wifi','s1','Wi‑Fi gratuito','In tutte le camere e negli spazi comuni.'),
 ('coffee','s2','Colazione','Caffè napoletano e dolci della tradizione.'),
 ('snow','s3','Aria condizionata','Climatizzazione regolabile in camera.'),
 ('bell','s4','Accoglienza','Reception e assistenza per ogni esigenza.'),
 ('map','s5','Consigli locali','Itinerari, ristoranti e segreti di Napoli.'),
 ('bag','s6','Deposito bagagli','Per goderti la città fino all’ultimo minuto.'),
 ('car','s7','Transfer su richiesta','Da e per aeroporto, stazione e porto.'),
 ('spark','s8','Pulizia quotidiana','Camere sempre fresche e ordinate.')]
serv=''
for ic,k,t,d in SERV:
    serv += f'<li class="service glow-card"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{IC[ic]}</svg><h3 data-i18n="services.{k}t">{t}</h3><p data-i18n="services.{k}d">{d}</p></li>\n      '

NAP = [('n1','Centro Storico UNESCO','Spaccanapoli, San Gregorio Armeno e i vicoli dove la città vive da oltre 2500 anni.'),
 ('n2','Cappella Sansevero','Il Cristo Velato, uno dei capolavori della scultura di ogni tempo.'),
 ('n3','Museo Archeologico Nazionale','Tesori di Pompei ed Ercolano in uno dei musei più importanti al mondo.'),
 ('n4','Lungomare e Castel dell’Ovo','Passeggiate sul golfo, il Vesuvio di fronte e tramonti indimenticabili.'),
 ('n5','Pizza, sfogliatella e caffè','La cucina napoletana, patrimonio di gusto: l’arte del pizzaiuolo è UNESCO.'),
 ('n6','Teatro di San Carlo','Il più antico teatro d’opera d’Europa ancora in attività.'),
 ('n7','Vesuvio e Pompei','Il vulcano del nostro simbolo e le città romane ai suoi piedi.'),
 ('n8','Capri, Ischia e Procida','Le isole del golfo, raggiungibili in traghetto o aliscafo.')]
nap=''
for i,(k,t,d) in enumerate(NAP):
    nap += f'<li class="nap glow-card"><span class="nap-num" aria-hidden="true">{i+1:02d}</span><h3 data-i18n="naples.{k}t">{t}</h3><p data-i18n="naples.{k}d">{d}</p></li>\n      '

GAL = [('galleria-ingresso','g1',"L’ingresso con le lanterne",'wide'),
 ('galleria-camera','g2','Camere luminose',''),
 ('galleria-colazione','g3','Colazione napoletana',''),
 ('galleria-vicoli','g5','I vicoli del centro',''),
 ('galleria-golfo','g4','Il golfo al tramonto','tall'),
 ('galleria-notte','g6','Quando Napoli si accende','wide')]
gal=''
for img,k,cap,cls in GAL:
    gal += f'''<figure class="gal {cls} reveal"><img src="img/{img}.svg"{' style="object-position:50% 15%"' if img=='galleria-ingresso' else ''} alt="{cap} — illustrazione segnaposto" data-i18n-attr="alt:gallery.{k}alt" width="1200" height="800" loading="lazy" decoding="async"><figcaption><span data-i18n="gallery.{k}">{cap}</span><small data-i18n="photoBadge">Foto reale in arrivo</small></figcaption></figure>
      '''

random.seed(3)
refl = ''.join(f'<rect class="rf" x="{685-(16+i*12)/2 + random.uniform(-6,6):.0f}" y="{776+i*9}" width="{16+i*12 + random.uniform(-8,8):.0f}" height="3" rx="1.5" fill="#F6D9A0" opacity="{0.7-i*0.05:.2f}"/>' for i in range(13))

MEL = '''<svg class="melodia-sym" viewBox="5 12 190 135" aria-hidden="true" focusable="false"><path d="M118,18 a40,40 0 1 0 34,62 a32,32 0 1 1 -34,-62z" fill="#C8CCD2"/><g fill="none" stroke="#C9A24A" stroke-width="2.4" stroke-linecap="round">''' + ''.join(f'<path d="M10,{104+i*9} q22,-10 45,0 t45,0 t45,0 t45,0"/>' for i in range(5)) + '''</g><circle cx="58" cy="113" r="5" fill="#D9735B"/><path d="M63,113 V92" stroke="#D9735B" stroke-width="2"/><circle cx="146" cy="122" r="5" fill="#D9735B"/><path d="M151,122 V101" stroke="#D9735B" stroke-width="2"/></svg>'''

MAP = '''<svg viewBox="0 0 400 260" aria-hidden="true" focusable="false"><rect width="400" height="260" fill="var(--map-sea)"/><path d="M0,40 C60,60 90,30 140,70 C180,100 200,140 250,150 C300,160 330,190 400,200 V0 H0Z" fill="var(--map-land)"/><path d="M0,40 C60,60 90,30 140,70 C180,100 200,140 250,150 C300,160 330,190 400,200" fill="none" stroke="#C9A24A" stroke-width="2"/><g stroke="var(--map-road)" stroke-width="1.5" fill="none" opacity=".7"><path d="M20,10 L150,90 M60,0 L120,120 M180,20 L170,110 M220,0 L300,140 M100,40 L300,40"/></g><path d="M330,120 C345,108 352,100 360,92 L366,92 C372,100 380,110 392,120" fill="none" stroke="#C9A24A" stroke-width="2.5"/><g transform="translate(160,92)"><circle r="22" fill="#C9A24A" opacity=".25"><animate attributeName="r" values="10;26;10" dur="3s" repeatCount="indefinite"/></circle><path d="M0,0 C-9,-10 -12,-15 -12,-21 a12,12 0 0 1 24,0 c0,6 -3,11 -12,21z" fill="#B5553A"/><circle cy="-21" r="4.5" fill="#F7F3EA"/></g></svg>'''

t = open(os.path.join(D,'index.template.html')).read()
SPRITE = f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs><clipPath id="logo-clip" clipPathUnits="userSpaceOnUse"><path d="{PROF} L885,0 L315,0 Z"/></clipPath></defs></svg>'
t = t.replace('<body>\n', '<body>\n'+SPRITE+'\n', 1)
for k,v in {'LOGO_SMALL':LOGO,'WA_ICON':WA,'ROOMS':rooms,'SERVICES':serv,'NAPLES':nap,'GALLERY':gal,'PROF':PROF,'RAYS':RAYS,'REFLECTION':refl,'MELODIA_SYMBOL':MEL,'MAP_ART':MAP}.items():
    t = t.replace('{{'+k+'}}', v)
assert '{{' not in t
open(os.path.join(D,'index.html'),'w').write(t)
print('index.html ok', len(t))
