"""Screenshot desktop/mobile + controllo errori console. Avvia prima: python3 -m http.server 8765"""
import os, sys
from playwright.sync_api import sync_playwright
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
URL = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/index.html'
OUT = os.path.join(D, 'screenshots'); os.makedirs(OUT, exist_ok=True)
errors = []
def run(pg, name, w, h, scheme='light'):
    pg.emulate_media(color_scheme=scheme)
    pg.goto(URL, wait_until='networkidle')
    pg.wait_for_timeout(4200)  # animazione alba
    pg.screenshot(path=f'{OUT}/{name}-hero.png')
    # notte: scroll a metà hero
    pg.evaluate('window.scrollTo(0, innerHeight*0.5)'); pg.wait_for_timeout(700)
    pg.screenshot(path=f'{OUT}/{name}-hero-tramonto.png')
    pg.evaluate('window.scrollTo(0, innerHeight*1.0)'); pg.wait_for_timeout(900)
    pg.screenshot(path=f'{OUT}/{name}-hero-notte.png')
    # scorri tutta la pagina per attivare le animazioni
    hgt = pg.evaluate('document.documentElement.scrollHeight')
    for y in range(0, hgt, h//2):
        pg.evaluate(f'window.scrollTo(0,{y})'); pg.wait_for_timeout(120)
    pg.wait_for_timeout(1200)
    pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(800)
    # per la cattura a pagina intera disattiva il 'pin' dell'hero (in navigazione reale resta attivo)
    pg.add_style_tag(content='.hero{height:100vh!important}.hero-stage{position:relative!important}')
    pg.wait_for_timeout(300)
    pg.screenshot(path=f'{OUT}/{name}-pagina-intera.png', full_page=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, w, h, mob, scheme in [('desktop-1440', 1440, 900, False, 'light'), ('mobile-390', 390, 844, True, 'light')]:
        ctx = b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1 if not mob else 2, is_mobile=mob, has_touch=mob)
        pg = ctx.new_page()
        pg.on('console', lambda m, n=name: m.type in ('error', 'warning') and errors.append(f'[{n}] {m.type}: {m.text}'))
        pg.on('pageerror', lambda e, n=name: errors.append(f'[{n}] pageerror: {e}'))
        pg.on('requestfailed', lambda r, n=name: errors.append(f'[{n}] requestfailed: {r.url}'))
        run(pg, name, w, h, scheme)
        ctx.close()
    b.close()
print('ERRORI:' if errors else 'Nessun errore in console.')
for e in errors: print(' ', e)
