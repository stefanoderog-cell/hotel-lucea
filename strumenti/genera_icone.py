"""Genera icone PNG (PWA) da img/favicon.svg con Chromium headless (playwright)."""
import os
from playwright.sync_api import sync_playwright
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
fav = 'file://' + D + '/img/favicon.svg'
jobs = [('icon-192.png',192,0,True),('icon-512.png',512,0,True),('apple-touch-icon.png',180,0,False),('icon-maskable-512.png',512,0.12,False)]
with sync_playwright() as p:
    b = p.chromium.launch()
    for name,s,pad,transparent in jobs:
        pg = b.new_page(viewport={'width':s,'height':s})
        inner = int(s*(1-2*pad))
        bg = 'transparent' if transparent else '#1F3A5F'
        pg.set_content(f'<html><body style="margin:0;background:{bg};display:grid;place-items:center;width:{s}px;height:{s}px"><img src="{fav}" width="{inner}" height="{inner}" style="{"border-radius:0" if pad else ""}"></body></html>')
        pg.wait_for_timeout(200)
        pg.screenshot(path=os.path.join(D,'img',name), omit_background=transparent)
        pg.close()
    b.close()
print('icone ok')
