# Tennis

Et 16-bit tennisspil til mobil og browser med SNES-tennis som forbillede: kameraet bag banen, fire slagknapper, retningsstyret sigte og rigtig tennistælling. v2.13.

**Spil:** åbn `index.html`, eller slå GitHub Pages til (Settings → Pages → Branch `main`, mappe `/root`). På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## Indhold
- Pixelgrafik i 16-bit-stil med mode 7-bane, publikum og dommer
- Opvisning med top 64 fra ATP eller WTA (vælg begge spillere) og de fire Grand Slams (Australian Open, Roland-Garros, Wimbledon, US Open) med 128 spillere og 7 runder
- Herre- eller damesingle med top 64 fra ATP- og WTA-ranglisten (19. okt. 2026) plus 64 tilfældige kvalifikanter
- Du spiller selv som en af top 64 i både opvisning og Grand Slam (med spillerens seedning)
- Hardcourt, grus og græs med forskelligt hop og fart
- Serv fra baglinjen over i feltet på skrå med sigtemarkering; serven skifter hvert parti
- Indstillinger i egen menu, gælder både opvisning og Grand Slam: 1, 3 eller 5 sæt · 2, 4 eller 6 partier pr. sæt · tiebreak til/fra
- 4 sværhedsgrader, 3 tempi, løbehjælp (fra / hjælp / fuld)

## Styring
| Knap | Tastatur | Slag |
|---|---|---|
| B | J · Z · Mellemrum | Hårdt slag: tryk = ketsjer tilbage, slip = slag (hold for mere fart) / hård serv |

| Y | K · X · L · C | Lob / sikker kick-serv |

Pile eller WASD flytter spilleren og sigter: op slår dybt, ned slår kort, venstre/højre mod siden. P eller Esc pauser, F giver fuld skærm. Gamepad virker også.

## Filer
- `index.html` – hele spillet i én fil
- `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` – app-ikon og fuldskærm på mobil

## Udvikling
Kilden ligger i `src/game.html`. `python3 build.py` bygger `index.html` (GitHub-versionen) og artifakt-versionen ud fra den.

## Versioner
Hver udgave gemmes også som `versions/tennis-vX.Y.html`, og versionen står i titlen og på startskærmen.
