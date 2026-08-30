# Figures

Save your images here using exactly these filenames. `.jpg` or `.png` both work — if you
use `.png`, update the `src` in `index.html` to match.

## LPBF 316L stainless steel section

| Filename        | What it should show                                  |
|-----------------|------------------------------------------------------|
| `lpbf-01.jpg`   | Microstructure of LPBF 316L                          |
| `lpbf-02.jpg`   | Tensile / stress–strain response at 850 °C           |
| `lpbf-03.jpg`   | Vertical vs. horizontal build orientation comparison |

## Creep–fatigue section

| Filename                       | What it should show                          |
|--------------------------------|----------------------------------------------|
| `blade-failure-modes.jpg`      | Failure modes in turbine blades              |
| `blade-failure-locations.jpg`  | Probable blade failure locations             |
| `rve-validation.jpg`           | RVE-level validation of creep–fatigue        |
| `blade-failure-sites.jpg`      | Sites where the blade generally fails        |

## Adding more

To add a fourth figure to a section, copy one `<figure>` block inside the matching
`<div class="figs">` in `index.html` and change the `src`, `alt` and caption. The grid
reflows on its own.

Keep images under roughly 400 KB each so the pages stay fast. Exporting at about
1200 px wide is plenty.
