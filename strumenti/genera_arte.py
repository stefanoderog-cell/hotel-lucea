#!/usr/bin/env python3
"""Genera le illustrazioni SVG segnaposto (stile del marchio Lucea).
Sostituire con le foto reali dell'hotel quando disponibili."""
import os, random, math
OUT = os.path.join(os.path.dirname(__file__), '..', 'img')
os.makedirs(OUT, exist_ok=True)
GOLD='#C9A24A'; BLU='#1F3A5F'; TUFO='#E8D3A8'; CALCE='#F7F3EA'; TERRA='#B5553A'; ARG='#C8CCD2'
# Profilo Somma–Vesuvio dal file di produzione dell'insegna (coordinate originali)
PROF = "M315.0,296 C375.0,292 435.0,256 476.0,242 C494.0,235 512.0,235 526.0,244 C542.0,252 560.0,256 580.0,256 C600.0,256 622.0,234 636.0,218 L641.0,213 L677.0,213 L682.0,218 C702.0,240 750.0,274 805.0,287 C838.0,294 862.0,296 885.0,296"

DEFS = f'''<defs>
<linearGradient id="ott" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0D9A0"/><stop offset=".45" stop-color="#D8B464"/><stop offset="1" stop-color="#9A7731"/></linearGradient>
<linearGradient id="tram" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A4A72"/><stop offset=".55" stop-color="#C77A55"/><stop offset="1" stop-color="#F2C98A"/></linearGradient>
<linearGradient id="notte" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B1626"/><stop offset=".7" stop-color="#1F3A5F"/><stop offset="1" stop-color="#3B4E6B"/></linearGradient>
<linearGradient id="mare" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2B5079"/><stop offset="1" stop-color="#14263F"/></linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#FFD89A" stop-opacity=".9"/><stop offset="1" stop-color="#FFD89A" stop-opacity="0"/></radialGradient>
<linearGradient id="piperno" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6E6E6A"/><stop offset="1" stop-color="#4C4C4A"/></linearGradient>
</defs>'''

def svg(w,h,body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title>{DEFS}{body}</svg>'

def vesuvio(x,y,s,fill,stroke=GOLD,sw=3):
    # posiziona il profilo (base y=296, centro x=600) in (x,y) con scala s
    return (f'<g transform="translate({x},{y}) scale({s}) translate(-600,-296)">'
            f'<path d="{PROF} L885,330 L315,330 Z" fill="{fill}"/>'
            f'<path d="{PROF}" fill="none" stroke="{stroke}" stroke-width="{sw/s:.2f}" stroke-linecap="round"/></g>')

def sole(cx,cy,r,rays=True):
    out = f'<circle cx="{cx}" cy="{cy}" r="{r*3}" fill="url(#glow)" opacity=".6"/>'
    if rays:
        for i in range(11):
            a = math.pi*(0.08+0.84*i/10)
            r1, r2 = r*1.25, r*(1.7 if i%2==0 else 1.5)
            out += f'<line x1="{cx-r1*math.cos(a):.1f}" y1="{cy-r1*math.sin(a):.1f}" x2="{cx-r2*math.cos(a):.1f}" y2="{cy-r2*math.sin(a):.1f}" stroke="url(#ott)" stroke-width="{r*0.07:.1f}" stroke-linecap="round"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#ott)"/>'
    return out

random.seed(7)
def luci(n,x0,x1,y0,y1,col='#FFD27A'):
    return ''.join(f'<circle cx="{random.uniform(x0,x1):.0f}" cy="{random.uniform(y0,y1):.0f}" r="{random.uniform(1.2,2.8):.1f}" fill="{col}" opacity="{random.uniform(.5,1):.2f}"/>' for _ in range(n))

def onde(y,w,col,op=.35,n=14):
    return ''.join(f'<path d="M{random.uniform(0,w):.0f},{y+i*14} q20,-6 40,0" stroke="{col}" stroke-width="2" fill="none" opacity="{op}"/>' for i in range(n) for _ in range(2))

W,H=1200,800
arts = {}
# 1 golfo al tramonto
b = f'<rect width="{W}" height="{H}" fill="url(#tram)"/>' + sole(628,478,62) + vesuvio(640,520,1.35,'#5B3F3A',GOLD,3)
b += f'<rect y="520" width="{W}" height="280" fill="url(#mare)"/>'
b += ''.join(f'<rect x="{620-i*9}" y="{530+i*16}" width="{40+i*18}" height="4" rx="2" fill="#F2C98A" opacity="{.7-i*.05:.2f}"/>' for i in range(12))
b += '<path d="M150,640 l70,0 l-12,16 l-48,0z M185,640 l0,-60 l28,52z" fill="#14263F"/>'
b += '<path d="M930,700 l90,0 l-14,18 l-62,0z M975,700 l0,-70 l32,62z" fill="#14263F"/>'
arts['galleria-golfo'] = ('Golfo di Napoli al tramonto con il Vesuvio (illustrazione segnaposto)', b)
# 2 ingresso con lanterne (piperno, arco bianco)
b = f'<rect width="{W}" height="{H}" fill="url(#piperno)"/>'
for r in range(0,H,64):
    off = 0 if (r//64)%2==0 else 90
    for c in range(-off,W,180):
        b += f'<rect x="{c+2}" y="{r+2}" width="176" height="60" fill="#5d5d5a" stroke="#4a4a47" stroke-width="2" opacity=".55"/>'
b += '<path d="M420,800 L420,380 A180,180 0 0 1 780,380 L780,800 Z" fill="#F4EFE4"/>'
b += '<path d="M450,800 L450,385 A150,150 0 0 1 750,385 L750,800 Z" fill="#2B2420"/>'
b += '<path d="M600,800 V240" stroke="#3a302a" stroke-width="4" opacity=".0"/>'
b += f'<path d="M450,385 A150,150 0 0 1 750,385" fill="none" stroke="{GOLD}" stroke-width="3" opacity=".7"/>'
for x in (300,900):
    b += f'<circle cx="{x}" cy="420" r="140" fill="url(#glow)" opacity=".75"/>'
    b += f'<path d="M{x-6},300 h12 v30 h-12z" fill="#1a1a1a"/><path d="M{x-34},330 h68 l-10,110 h-48z" fill="#FFD58A" stroke="#1a1a1a" stroke-width="7"/><path d="M{x-40},325 h80 l-12,-18 h-56z M{x-30},440 h60 v12 h-60z" fill="#1a1a1a"/>'
for x in (330,870):
    b += f'<rect x="{x-60}" y="700" width="120" height="100" fill="#3d3631"/><ellipse cx="{x}" cy="690" rx="85" ry="55" fill="#4F6B3E"/><ellipse cx="{x-25}" cy="670" rx="45" ry="35" fill="#5f7d4a"/>'
b += f'<rect x="440" y="120" width="320" height="120" fill="#2c2a28" stroke="{BLU}" stroke-width="10"/>' + vesuvio(600,195,0.42,'none',GOLD,3) + sole(588,185,14,False)
b += f'<text x="600" y="228" text-anchor="middle" font-family="Georgia,serif" font-size="26" letter-spacing="8" fill="{GOLD}">LUCEA</text>'
arts['galleria-ingresso'] = ("L'ingresso con le lanterne e l'insegna in pietra lavica (illustrazione segnaposto)", b)
# 3 camera con finestra sul Vesuvio
def camera(vista='vesuvio', accento=TERRA, letto_col=CALCE, title=''):
    b = f'<rect width="{W}" height="{H}" fill="{TUFO}"/><rect y="600" width="{W}" height="200" fill="#B99C72"/>'
    b += ''.join(f'<path d="M0,{600+i*40} H{W}" stroke="#a88b62" stroke-width="2"/>' for i in range(1,5))
    # finestra
    b += f'<rect x="700" y="110" width="380" height="380" fill="#F4EFE4"/>'
    sky = 'url(#tram)' if vista!='notte' else 'url(#notte)'
    b += f'<svg x="720" y="130" width="340" height="340" viewBox="0 0 340 340"><rect width="340" height="340" fill="{sky}"/>'
    if vista=='notte':
        b += luci(40,0,340,0,180,'#F7F3EA') + vesuvio(170,250,0.62,'#0F1C2E',GOLD,2) + f'<rect y="250" width="340" height="90" fill="#0F1C2E"/>' + luci(60,0,340,255,320)
    elif vista=='mare':
        b += sole(120,220,26) + f'<rect y="220" width="340" height="120" fill="url(#mare)"/>' + vesuvio(230,222,0.45,'#4D3B3A',GOLD,2)
    else:
        b += sole(166,250,30) + vesuvio(170,252,0.62,'#5B3F3A',GOLD,2) + f'<rect y="252" width="340" height="88" fill="url(#mare)"/>'
    b += '</svg>'
    b += f'<path d="M890,110 V490 M700,300 H1080" stroke="#F4EFE4" stroke-width="12"/>'
    b += f'<path d="M640,90 h40 v430 h-40z M1120,90 h-40 v430 h40z" fill="{accento}" opacity=".85"/>'
    # letto
    b += f'<rect x="90" y="330" width="520" height="140" rx="10" fill="#6B4B32"/>'
    b += f'<rect x="70" y="440" width="560" height="170" rx="16" fill="{letto_col}"/><rect x="70" y="520" width="560" height="90" rx="12" fill="{BLU}"/>'
    b += f'<path d="M70,520 H630" stroke="{GOLD}" stroke-width="5"/>'
    b += f'<rect x="120" y="400" width="190" height="70" rx="30" fill="#fffaf0"/><rect x="390" y="400" width="190" height="70" rx="30" fill="#fffaf0"/>'
    # lampada
    b += f'<circle cx="40" cy="300" r="120" fill="url(#glow)" opacity=".6"/><path d="M15,250 h50 l15,60 h-80z" fill="#F2D59A"/><rect x="36" y="310" width="8" height="200" fill="{GOLD}"/>'
    b += f'<rect y="610" x="0" width="{W}" height="6" fill="#00000010"/>'
    return (title, b)
arts['galleria-camera'] = camera('mare', GOLD, TUFO, 'Camera luminosa con vista sul Vesuvio (illustrazione segnaposto)')
# 4 colazione: caffè e sfogliatella su maiolica
b = f'<rect width="{W}" height="{H}" fill="{CALCE}"/>'
for i in range(0,W,100):
    for j in range(0,H,100):
        b += f'<g transform="translate({i},{j})"><rect width="100" height="100" fill="#F4EFE4" stroke="#d9cfbd"/><circle cx="50" cy="50" r="26" fill="none" stroke="#3E6E9E" stroke-width="5" opacity=".55"/><path d="M50,14 L58,50 L50,86 L42,50Z M14,50 L50,42 L86,50 L50,58Z" fill="#E2B34A" opacity=".55"/></g>'
b += '<ellipse cx="430" cy="470" rx="230" ry="80" fill="#00000022"/><ellipse cx="420" cy="440" rx="220" ry="80" fill="#fff" stroke="#e6dccb" stroke-width="4"/>'
b += '<path d="M330,320 h180 l-20,140 q-70,24 -140,0z" fill="#fff" stroke="#e6dccb" stroke-width="4"/><path d="M505,350 q60,0 40,50 q-15,25 -45,22" fill="none" stroke="#fff" stroke-width="16"/><ellipse cx="420" cy="322" rx="90" ry="20" fill="#5A3420"/><ellipse cx="420" cy="320" rx="70" ry="13" fill="#B07A4C"/>'
b += '<path d="M400,270 q-20,-30 0,-60 q20,-30 0,-60 M440,280 q-20,-30 0,-60 q20,-30 0,-60" stroke="#bfb3a3" stroke-width="5" fill="none" opacity=".6"/>'
b += '<ellipse cx="820" cy="520" rx="210" ry="70" fill="#00000022"/><ellipse cx="810" cy="490" rx="200" ry="70" fill="#fff" stroke="#e6dccb" stroke-width="4"/>'
b += '<path d="M700,490 Q720,380 820,370 Q920,380 930,490 Q820,520 700,490Z" fill="#D9A55A"/>' + ''.join(f'<path d="M{730+i*22},{485-abs(5-i)*2} Q{800+i*4},{380+abs(5-i)*3} {820+i*10},{372+abs(5-i)}" stroke="#A86E2E" stroke-width="3" fill="none"/>' for i in range(9))
b += '<path d="M690,490 Q820,530 940,490" stroke="#fff" stroke-width="6" fill="none" opacity=".7"/>'
arts['galleria-colazione'] = ('Colazione napoletana: caffè e sfogliatella (illustrazione segnaposto)', b)
# 5 vicoli
b = f'<rect width="{W}" height="{H}" fill="url(#tram)"/>'
b += '<path d="M0,0 H420 L520,800 H0Z" fill="#C98A5E"/><path d="M1200,0 H780 L680,800 H1200Z" fill="#D9A36E"/>'
for y in range(80,700,120):
    b += f'<rect x="{150+y*0.1:.0f}" y="{y}" width="90" height="70" fill="#5A3A2A"/><rect x="{960-y*0.1:.0f}" y="{y}" width="90" height="70" fill="#5A3A2A"/>'
    b += f'<rect x="{155+y*0.1:.0f}" y="{y+5}" width="80" height="60" fill="#FFD58A" opacity="{.25+((y//120)%2)*.6:.2f}"/>'
for k,y in enumerate((170,330,470)):
    b += f'<path d="M{420+y*0.12:.0f},{y} Q600,{y+60} {780-y*0.12:.0f},{y}" stroke="#3a2a22" stroke-width="2" fill="none"/>'
    cols = [CALCE,TERRA,'#3E6E9E',TUFO,CALCE,'#D9735B']
    for i in range(6):
        x = 470+y*0.1+i*(260-y*0.2)/6
        b += f'<rect x="{x:.0f}" y="{y+18+abs(2.5-i)*-7+20:.0f}" width="30" height="{40+(i%3)*10}" fill="{cols[(i+k)%6]}"/>'
b += luci(30,520,680,560,780,'#FFD58A') + f'<path d="M520,800 L560,520 H640 L680,800Z" fill="#7a5a44" opacity=".35"/>'
arts['galleria-vicoli'] = ('Vicoli del centro storico con i panni stesi (illustrazione segnaposto)', b)
# 6 golfo di notte
b = f'<rect width="{W}" height="{H}" fill="url(#notte)"/>' + luci(120,0,W,0,380,'#F7F3EA')
b += f'<circle cx="980" cy="150" r="46" fill="{ARG}"/><circle cx="1000" cy="138" r="44" fill="#13243b"/>'
b += vesuvio(600,520,1.4,'#0E1A2B',GOLD,2.5) + f'<rect y="520" width="{W}" height="280" fill="#0E1A2B"/>'
b += luci(220,0,W,505,535) + ''.join(f'<rect x="{random.uniform(0,W):.0f}" y="{random.uniform(560,780):.0f}" width="{random.uniform(10,40):.0f}" height="2" fill="#FFD27A" opacity="{random.uniform(.2,.6):.2f}"/>' for _ in range(90))
arts['galleria-notte'] = ('Il golfo di notte: Napoli si accende (illustrazione segnaposto)', b)
# camere
arts['camera-classica'] = camera('vesuvio', TERRA, CALCE, 'Camera Classica (illustrazione segnaposto)')
arts['camera-superior'] = camera('mare', '#3E6E9E', CALCE, 'Superior Vista (illustrazione segnaposto)')
arts['camera-junior'] = camera('notte', GOLD, TUFO, 'Junior Suite (illustrazione segnaposto)')
arts['camera-familiare'] = camera('vesuvio', '#D9735B', '#F4EFE4', 'Camera Familiare (illustrazione segnaposto)')

for name,(title,body) in arts.items():
    with open(os.path.join(OUT, name+'.svg'),'w') as f: f.write(svg(W,H,body,title))
print('ok', len(arts))
