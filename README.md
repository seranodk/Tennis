# Tennis

Et 16-bit tennisspil til mobil og browser med SNES-tennis som forbillede: kameraet bag banen, fire slagknapper, retningsstyret sigte og rigtig tennistælling. v1.0.

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

## Udvikling
Kilden ligger i `src/game.html`. `python3 build.py` bygger `index.html` (GitHub-versionen) og artifakt-versionen ud fra den.
