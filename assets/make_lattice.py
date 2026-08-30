"""Generate assets/lattice.svg - an edge dislocation in a lattice.

Below the slip plane: 13 atomic columns.
Above the slip plane: 14 columns - the extra half-plane that IS the dislocation.
"""

W, H = 640, 300
SLIP_Y = 152
X0, X1 = 36, 604

ROWS_UP = [138, 106, 74, 42]
ROWS_DOWN = [168, 200, 232, 264]

N_DOWN = 13
N_UP = 14

INK = "#3A424B"
SLIP = "#1C6B5A"
HEAT = "#A6702B"

CORE_X = X0 + (X1 - X0) * 0.5


def cols(n):
    step = (X1 - X0) / (n - 1)
    return [X0 + i * step for i in range(n)]


atoms = []
for y in ROWS_DOWN:
    for x in cols(N_DOWN):
        atoms.append((x, y, False))
for y in ROWS_UP:
    for x in cols(N_UP):
        atoms.append((x, y, True))

parts = []
for x, y, above in atoms:
    d = abs(x - CORE_X) / (X1 - X0)          # 0 at core, 0.5 at edges
    near = d < 0.075 and above
    r = 5.2 if not near else 5.8
    fill = SLIP if near else INK
    op = 0.9 if near else 0.5
    delay = round(0.15 + d * 1.5, 2)
    parts.append(
        f'<circle cx="{x:.1f}" cy="{y}" r="{r}" fill="{fill}" '
        f'opacity="{op}" style="--d:{delay}s"/>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     role="img" aria-label="Edge dislocation: an extra half-plane of atoms terminating on the slip plane.">
  <style>
    circle {{ animation: pop .5s cubic-bezier(.2,.8,.3,1) both; animation-delay: var(--d, 0s); }}
    .trace {{ stroke-dasharray: 580; stroke-dashoffset: 580; animation: draw 1.4s ease-out 1.0s forwards; }}
    .mark  {{ opacity: 0; animation: fade .6s ease-out 2.1s forwards; }}
    .burg  {{ opacity: 0; animation: fade .6s ease-out 2.4s forwards; }}
    @keyframes pop  {{ from {{ opacity: 0; transform: translateY(6px); }} }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes fade {{ to {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{
      circle, .trace, .mark, .burg {{ animation: none; opacity: inherit; stroke-dashoffset: 0; }}
      .mark, .burg {{ opacity: 1; }}
      circle {{ transform: none; }}
    }}
  </style>
  <line class="trace" x1="{X0 - 14}" y1="{SLIP_Y}" x2="{X1 + 14}" y2="{SLIP_Y}"
        stroke="{SLIP}" stroke-width="1.25" stroke-dasharray="580" opacity=".55"/>
{chr(10).join("  " + p for p in parts)}
  <g class="mark" stroke="{SLIP}" stroke-width="2.4" stroke-linecap="round">
    <line x1="{CORE_X:.1f}" y1="{SLIP_Y - 46}" x2="{CORE_X:.1f}" y2="{SLIP_Y}"/>
    <line x1="{CORE_X - 15:.1f}" y1="{SLIP_Y}" x2="{CORE_X + 15:.1f}" y2="{SLIP_Y}"/>
  </g>
  <g class="burg">
    <line x1="{CORE_X + 26:.1f}" y1="{SLIP_Y + 22}" x2="{CORE_X + 74:.1f}" y2="{SLIP_Y + 22}"
          stroke="{HEAT}" stroke-width="1.8"/>
    <path d="M{CORE_X + 74:.1f},{SLIP_Y + 22} l-8,-4.5 v9 z" fill="{HEAT}"/>
    <text x="{CORE_X + 44:.1f}" y="{SLIP_Y + 14}" fill="{HEAT}"
          font-family="ui-monospace, monospace" font-size="14" font-style="italic">b</text>
  </g>
</svg>
'''

with open("/home/claude/site/assets/lattice.svg", "w") as f:
    f.write(svg)
print("wrote lattice.svg", len(svg), "bytes")
