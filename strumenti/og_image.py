"""Genera img/og-image.png (1200x630) dall'hero del sito. Richiede server locale su :8765."""
import os
from playwright.sync_api import sync_playwright
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1200,'height':630})
    pg.emulate_media(reduced_motion='reduce')
    pg.goto('http://localhost:8765/index.html', wait_until='networkidle')
    pg.add_style_tag(content='.site-header,.wa-float,.scroll-cue,.hero-lead,.hero-cta,.filament{display:none!important}.hero-copy{padding-top:70px!important}')
    pg.wait_for_timeout(800); pg.screenshot(path=os.path.join(D,'img','og-image.png')); b.close()
print('og ok')
