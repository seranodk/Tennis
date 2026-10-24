#!/usr/bin/env python3
"""Builds the artifact page and the GitHub Pages bundle from src/game.html."""
import json, os, shutil
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ROOT, 'src/game.html'), encoding='utf-8').read()
VERSION = 'v1.0'

# --- artifact version: page body only (the artifact host adds the skeleton)
os.makedirs(os.path.join(ROOT, 'artifact'), exist_ok=True)
open(os.path.join(ROOT, 'artifact/tennis.html'), 'w', encoding='utf-8').write(src)

# --- GitHub Pages version
out = os.path.join(ROOT, '.')
os.makedirs(out, exist_ok=True)
head = f'''<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#0b1230">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Tennis">
<meta name="description" content="Tennis – 16-bit tennisspil til mobil og browser ({VERSION})">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
'''
body = src.replace('<title>Tennis</title>', '<title>Tennis</title>', 1)
# split: everything up to </style> goes in head, rest in body
i = body.index('</style>') + len('</style>')
page = head + body[:i] + '\n</head>\n<body>\n' + body[i:] + '\n</body>\n</html>\n'
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)

manifest = {
    "name": "Tennis", "short_name": "Tennis", "description": "16-bit tennisspil",
    "start_url": "./", "scope": "./", "display": "fullscreen", "orientation": "any",
    "background_color": "#0b1230", "theme_color": "#0b1230", "lang": "da",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}
json.dump(manifest, open(os.path.join(out, 'manifest.webmanifest'), 'w'), indent=2)
open(os.path.join(out, '.nojekyll'), 'w').write('')

def icon(n):
    s = 4 * n
    im = Image.new('RGB', (s, s), '#0b1230')
    d = ImageDraw.Draw(im)
    # court in perspective
    m = s * .14
    d.polygon([(s*.3, s*.22), (s*.7, s*.22), (s - m, s*.86), (m, s*.86)], fill='#2d68ad')
    w = max(2, s // 90)
    d.line([(s*.3, s*.22), (s*.7, s*.22), (s - m, s*.86), (m, s*.86), (s*.3, s*.22)], fill='#f3f6fa', width=w)
    d.line([(s*.5, s*.36), (s*.5, s*.70)], fill='#f3f6fa', width=w)
    d.rectangle([s*.2, s*.47, s*.8, s*.53], fill='#e8ecf4')
    r = s * .1
    cx, cy = s*.63, s*.33
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill='#d9f24a', outline='#55600a', width=w)
    return im.resize((n, n), Image.LANCZOS)

icon(192).save(os.path.join(out, 'icon-192.png'))
icon(512).save(os.path.join(out, 'icon-512.png'))
icon(180).save(os.path.join(out, 'apple-touch-icon.png'))

readme = f'''# Tennis

Et 16-bit tennisspil til mobil og browser med SNES-tennis som forbillede: kameraet bag banen, fire slagknapper, retningsstyret sigte og rigtig tennistælling. {VERSION}.

**Spil:** åbn `index.html`, eller slå GitHub Pages til (Settings → Pages → Branch `main`, mappe `/root`). På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## Indhold
- Opvisningskamp mod computeren og turnering med 4 turneringer × 3 runder og rankingpoint
- 8 spillere med hver sin stil (fart, kraft, kontrol, spin, serv)
- Hardcourt, grus og græs med forskelligt hop og fart
- 1, 3 eller 5 sæt · 2, 4 eller 6 partier pr. sæt · tiebreak til/fra
- 4 sværhedsgrader, 3 tempi, løbehjælp (fra / hjælp / fuld)

## Styring
| Knap | Tastatur | Slag |
|---|---|---|
| B | J · Z · Mellemrum | Flad / hård serv |
| A | K · X | Slice / skruet serv |
| X | I · C | Topspin / kick-serv |
| Y | U · V | Lob / sikker serv |

Pile eller WASD flytter spilleren og sigter: op slår dybt, ned slår kort, venstre/højre mod siden. P eller Esc pauser, F giver fuld skærm. Gamepad virker også.

## Filer
- `index.html` – hele spillet i én fil
- `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` – app-ikon og fuldskærm på mobil
'''
pass  # README vedligeholdes direkte i repoet
pass
print('built', VERSION)
