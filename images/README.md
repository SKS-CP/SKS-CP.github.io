# Images

Save your images here with exactly these filenames. `.jpg` or `.png` both work — if you
use `.png`, change the `src` in the HTML to match.

| Filename                       | Used on   | What it shows                                |
|--------------------------------|-----------|-----------------------------------------------|
| `photo.png`                    | Home      | Your photograph (portrait, about 400 px wide) |
| `blade-failure-modes.jpg`      | Research  | Failure modes in turbine blades               |
| `blade-failure-locations.jpg`  | Research  | Probable blade failure locations              |
| `rve-validation.jpg`           | Research  | RVE-level validation of creep–fatigue         |
| `blade-failure-sites.jpg`      | Research  | Sites where the blade generally fails         |
| `lpbf-01.jpg`                  | Research  | LPBF 316L microstructure                      |
| `lpbf-02.jpg`                  | Research  | Tensile response at 850 °C                    |
| `lpbf-03.jpg`                  | Research  | Vertical vs. horizontal build orientation     |

Until a file is added, a dashed "FIGURE" placeholder appears in its place, so nothing
looks broken.

To add another figure, copy one `<figure>` block inside the matching `<div class="figs">`
in `research.html` and change the `src`, `alt` and caption. The grid reflows on its own.

Keep each image under roughly 400 KB. Exporting at about 1200 px wide is plenty.
