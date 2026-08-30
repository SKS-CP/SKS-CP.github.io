import os

OUT = "/home/claude/site"

NAV = [
    ("index.html", "Home"),
    ("publications.html", "Publications"),
    ("code.html", "Code"),
    ("teaching.html", "Teaching"),
    ("contact.html", "Contact"),
]

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Bricolage+Grotesque:opsz,wght@12..96,400..700"
         "&family=IBM+Plex+Mono:wght@400;500"
         "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..600;1,8..60,400"
         "&display=swap")


def page(slug, title, description, body):
    items = "\n".join(
        '      <li><a href="{h}"{cur}>{l}</a></li>'.format(
            h=href, l=label,
            cur=' aria-current="page"' if href == slug else "")
        for href, label in NAV
    )
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="rail">
  <a class="mark" href="index.html">
    <span class="mark-name">Santosh<br>Kumar Shaw</span>
    <span class="mark-role">Research Scholar<br>Applied Mechanics, IIT Delhi</span>
  </a>
  <nav aria-label="Sections">
    <ul>
{items}
    </ul>
  </nav>
  <p class="rail-foot">
    Indian Institute of<br>Technology Delhi<br>
    <a href="mailto:amz228601@iitd.ac.in">amz228601@iitd.ac.in</a>
  </p>
</header>

<main id="main">
{body}
</main>
<script src="assets/site.js"></script>
</body>
</html>
'''


PUBLICATIONS = '''
  <p class="eyebrow">Peer-reviewed and preprint</p>
  <h1>Publications</h1>
  <p class="lede">Journal articles and preprints, newest first.</p>

  <ol class="pubs">
    <li>
      <h2 class="pub-title">
        <a href="https://doi.org/10.1016/j.addma.2026.105115">Orientation and strain-rate effects on high-temperature plasticity of 316L stainless steel fabricated by laser powder bed fusion</a>
      </h2>
      <p class="pub-meta">
        Additive Manufacturing &middot;
        <a href="https://doi.org/10.1016/j.addma.2026.105115">doi:10.1016/j.addma.2026.105115</a> &middot;
        <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=Wm7uCdcAAAAJ&amp;citation_for_view=Wm7uCdcAAAAJ:u5HHmVD_uO8C">Google Scholar</a>
      </p>
    </li>
    <li>
      <h2 class="pub-title">
        <a href="https://arxiv.org/abs/2605.23342">Studying creep–fatigue interaction of nickel-based superalloys using crystal plasticity and an entropy-based life prediction model</a>
      </h2>
      <p class="pub-meta">
        Preprint &middot;
        <a href="https://arxiv.org/abs/2605.23342">arXiv:2605.23342</a> &middot;
        <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=Wm7uCdcAAAAJ&amp;citation_for_view=Wm7uCdcAAAAJ:d1gkVwhDpl0C">Google Scholar</a>
      </p>
    </li>
  </ol>

  <p class="links" style="margin-top:2.5rem">
    <a href="https://scholar.google.com/citations?user=Wm7uCdcAAAAJ&amp;hl=en">Full list on Google Scholar</a>
  </p>
'''

CODE = '''
  <p class="eyebrow">Open code and data</p>
  <h1>Code</h1>
  <p class="lede">
    Model implementations and the supporting data behind the papers. Everything runs on
    MOOSE unless noted otherwise.
  </p>

  <div class="slab">
    <h2>CFI-CPFEM</h2>
    <a class="repo-link" href="https://github.com/SKS-CP/CFI-CPFEM">github.com/SKS-CP/CFI-CPFEM</a>
    <p>
      Dislocation density-based crystal plasticity finite element model for creep–fatigue
      interaction in single-crystal nickel superalloys, with the input decks and supporting
      data for the accompanying paper.
    </p>
  </div>

  <ul class="links" style="margin-top:2rem">
    <li><a href="https://github.com/SKS-CP">All repositories — github.com/SKS-CP</a></li>
  </ul>
'''

TEACHING = '''
  <p class="eyebrow">IIT Delhi</p>
  <h1>Teaching</h1>
  <p class="lede">
    Teaching assistantship: facilitated learning, graded assignments and supported faculty
    across the following undergraduate and postgraduate courses.
  </p>

  <ul class="courses">
    <li><span class="code">APL410</span><span class="name">Multiscale Modelling</span></li>
    <li><span class="code">AML8200</span><span class="name">Plasticity</span></li>
    <li><span class="code">APL380</span><span class="name">Biomechanics</span></li>
    <li><span class="code">APL103</span><span class="name">Experimental Methods</span></li>
    <li><span class="code">APL100</span><span class="name">Engineering Mechanics</span></li>
  </ul>
'''

CONTACT = '''
  <p class="eyebrow">Get in touch</p>
  <h1>Contact</h1>
  <p class="lede">
    Happy to hear about collaborations, questions on the models, or anything
    creep–fatigue related.
  </p>

  <ul class="detail">
    <li>
      <span class="k">Email</span>
      <span class="v"><a href="mailto:amz228601@iitd.ac.in">amz228601@iitd.ac.in</a></span>
    </li>
    <li>
      <span class="k">Phone</span>
      <span class="v"><a href="tel:+917001931050">+91 70019 31050</a></span>
    </li>
    <li>
      <span class="k">Office</span>
      <span class="v">
        <span>Research Scholar Room 4A/14, Block IV</span>
        <span>Dept. of Applied Mechanics, IIT Delhi</span>
        <span>New Delhi 110016, India</span>
      </span>
    </li>
    <li>
      <span class="k">Elsewhere</span>
      <span class="v">
        <span><a href="https://scholar.google.com/citations?user=Wm7uCdcAAAAJ&amp;hl=en">Google Scholar</a></span>
        <span><a href="https://www.linkedin.com/in/santosh-shaw-a13744275/">LinkedIn</a></span>
        <span><a href="https://github.com/SKS-CP">GitHub</a></span>
      </span>
    </li>
  </ul>

  <iframe class="map" title="Map of the Department of Applied Mechanics, IIT Delhi" loading="lazy"
    src="https://www.openstreetmap.org/export/embed.html?bbox=77.1877%2C28.5444%2C77.1957%2C28.5484&amp;layer=mapnik&amp;marker=28.5463655%2C77.1917207"></iframe>
  <p class="links" style="margin-top:.9rem">
    <a href="https://www.openstreetmap.org/?mlat=28.5463655&amp;mlon=77.1917207#map=17/28.54637/77.19172">Open larger map</a>
  </p>
'''

PAGES = [
    ("publications.html", "Publications — Santosh Kumar Shaw",
     "Journal articles and preprints by Santosh Kumar Shaw on crystal plasticity, "
     "creep-fatigue and additively manufactured metals.", PUBLICATIONS),
    ("code.html", "Code — Santosh Kumar Shaw",
     "Open-source crystal plasticity finite element models and supporting data.", CODE),
    ("teaching.html", "Teaching — Santosh Kumar Shaw",
     "Courses taught as a teaching assistant at IIT Delhi.", TEACHING),
    ("contact.html", "Contact — Santosh Kumar Shaw",
     "Contact details and office address at the Department of Applied Mechanics, IIT Delhi.",
     CONTACT),
]

for slug, title, desc, body in PAGES:
    with open(os.path.join(OUT, slug), "w") as f:
        f.write(page(slug, title, desc, body))
    print("wrote", slug)
