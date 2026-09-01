import html
import json
import os
import re

# Repository root: this script lives in <root>/assets/
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("index.html", "Home"),
    ("bio-sketch.html", "Bio-sketch"),
    ("research.html", "Research"),
    ("publications.html", "Publications"),
    ("teaching.html", "Teaching"),
    ("software.html", "Software"),
    ("contact.html", "Contact"),
]

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Roboto:ital,wght@0,400;0,500;0,700;1,400;1,700&display=swap")

SEARCH_ICON = (
    '<svg viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M15.5 14h-.79l-.28-.27A6.47 6.47 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16'
    'c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0'
    'C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>'
    '</svg>'
)


def page(slug, title, description, body):
    items = "\n".join(
        '        <li><a href="{h}"{cur}>{l}</a></li>'.format(
            h=href, l=label, cur=' aria-current="page"' if href == slug else "")
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

<div class="topbar">
  <div class="topbar-inner">
    <nav aria-label="Main">
      <ul>
{items}
      </ul>
    </nav>
    <button class="search-toggle" type="button" aria-expanded="false"
            aria-controls="site-search" aria-label="Search this site">{SEARCH_ICON}</button>
  </div>
  <div class="search-panel" id="site-search">
    <input type="search" placeholder="Search this site" aria-label="Search this site">
    <ul class="search-results"></ul>
  </div>
</div>

<div class="banner">
  <h1>Santosh Kumar Shaw</h1>
  <p>Applied Mechanics, IIT Delhi</p>
</div>

<main id="main">
  <div class="wrap">
{body}
  </div>
</main>

<footer class="foot">
  <div class="wrap">
    <p>Department of Applied Mechanics, Indian Institute of Technology Delhi,
       Hauz Khas, New Delhi 110016.</p>
  </div>
</footer>

<script src="assets/search-index.js"></script>
<script src="assets/site.js"></script>
</body>
</html>
'''


HOME = '''
    <div class="about">
      <div class="about-text">
        <h2>About me</h2>
        <p>
          I am a Research Scholar at the Department of Applied Mechanics at IIT Delhi. My
          research focuses on crystal plasticity, finite element analysis and
          creep&ndash;fatigue interaction. I work on decoding the complex mechanics of
          nickel-based superalloys using advanced frameworks such as MOOSE, to engineer a
          stronger and more resilient future. The work is multiscale, linking physics
          across spatial and temporal scales to simulate systems that no single scale
          can capture alone.
        </p>

        <p>My current research interests include problems in the following areas:</p>
        <ul class="interests">
          <li>Dislocation density-based crystal plasticity</li>
          <li>Creep&ndash;fatigue interaction in nickel-based superalloys</li>
          <li>Multiscale materials modelling</li>
          <li>High-temperature deformation of additively manufactured metals</li>
          <li>Damage modelling and life prediction</li>
        </ul>

        <p>My CV may be found <a href="files/cv.pdf">here</a>.</p>

        <p>
          <strong>Contact:</strong> Room 4A/14, Block IV, IIT Delhi, Hauz Khas,
          New Delhi 110016
        </p>

        <p>Email: <a href="mailto:amz228601@iitd.ac.in">amz228601@iitd.ac.in</a></p>

        <p class="inline-links">
          <a href="https://scholar.google.com/citations?user=Wm7uCdcAAAAJ&amp;hl=en">Google Scholar</a>
          <a href="https://www.linkedin.com/in/santosh-shaw-a13744275/">Linkedin</a>
          <a href="https://github.com/SKS-CP">Github</a>
        </p>

        <p class="callout">
          If you would like the models or the data behind the papers, please see
          <a href="software.html">Software</a>.
        </p>
      </div>

      <figure class="about-photo">
        <img src="images/photo.jpg" alt="Santosh Kumar Shaw">
      </figure>
    </div>

    <div class="band">
      <h2>What I work on</h2>
      <div class="cards">

        <div class="card">
          <h3>Creep&ndash;fatigue in turbine blades</h3>
          <p>
            A dislocation density-based crystal plasticity model, run in MOOSE, that finds
            where damage accumulates in a nickel superalloy blade and how long it survives.
          </p>
          <a class="more" href="research.html">See the research</a>
        </div>

        <div class="card">
          <h3>High-temperature plasticity of printed steel</h3>
          <p>
            How LPBF 316L behaves at 850&nbsp;&deg;C, and how much of that behaviour is
            inherited from the direction it was printed in.
          </p>
          <a class="more" href="publications.html">Read the paper</a>
        </div>

        <div class="card">
          <h3>Open models and data</h3>
          <p>
            The CFI-CPFEM implementation and the input decks behind the papers are public,
            so the results can be reproduced.
          </p>
          <a class="more" href="software.html">Browse the code</a>
        </div>

      </div>
    </div>
'''

BIO = '''
    <h2>Bio-sketch</h2>
    <p>
      I am a Research Scholar at the Department of Applied Mechanics, IIT Delhi, working on
      dislocation density-based crystal plasticity modelling of creep&ndash;fatigue
      interaction in single-crystal nickel superalloys.
    </p>

    <h3>Education</h3>
    <ul class="plain">
      <li>Ph.D. (ongoing), Applied Mechanics, Indian Institute of Technology Delhi</li>
      <li>M.Tech, Materials and Metallurgical Engineering, Jadavpur University</li>
      <li>B.Tech, Mechanical Engineering, Maulana Abul Kalam Azad University of
          Technology (MAKAUT, formerly WBUT), West Bengal</li>
    </ul>

    <h3>Research summary</h3>
    <p>
      My work sits between the microstructural and component scales. At the lower scale, a
      dislocation density-based constitutive model tracks the evolution of mobile and
      immobile dislocation populations on each slip system. At the upper scale, that model
      is driven through creep&ndash;fatigue load cycles in a finite element setting to
      predict where a turbine blade accumulates damage and how long it survives. The
      implementation is built on the MOOSE framework.
    </p>

    <h3>Skills and tools</h3>
    <ul class="interests">
      <li>MOOSE framework; finite element implementation of constitutive models</li>
      <li>Crystal plasticity, continuum plasticity, damage and life prediction</li>
      <li>C++, Python, high-performance and parallel computing</li>
      <li>Post-processing and visualisation of large simulation datasets</li>
    </ul>
'''

RESEARCH = '''
    <h2>Research</h2>
    <p>
      My research is multiscale. The two threads below run from the microstructure of the
      material up to the behaviour of the component it ends up in.
    </p>

    <h3>Creep&ndash;fatigue interaction in turbine blades made of nickel superalloys</h3>
    <p>
      Turbine blades fail where creep and fatigue act together. A dislocation
      density-based crystal plasticity model, implemented in MOOSE, is used to identify
      where that damage accumulates and to predict the remaining life of the blade. The
      model is validated first at the representative volume element (RVE) level and then
      applied at the component scale.
    </p>

    <div class="figs">
      <figure>
        <img src="images/blade-failure-modes.jpg" alt="Failure modes in turbine blades." loading="lazy">
        <figcaption>Failure modes in turbine blades.</figcaption>
      </figure>
      <figure>
        <img src="images/blade-failure-locations.jpg" alt="Probable failure locations on a turbine blade." loading="lazy">
        <figcaption>
          Probable locations of blade failure due to creep&ndash;fatigue interaction,
          corrosion, oxidation and other degradation mechanisms.
        </figcaption>
      </figure>
      <figure>
        <img src="images/rve-validation.jpg" alt="RVE-level validation of the creep-fatigue model." loading="lazy">
        <figcaption>Validation at the RVE level of creep&ndash;fatigue interaction.</figcaption>
      </figure>
      <figure>
        <img src="images/blade-failure-sites.jpg" alt="Sites where the blade generally fails." loading="lazy">
        <figcaption>Sites where the blade generally fails.</figcaption>
      </figure>
    </div>

    <h3>High-temperature plasticity of LPBF 316L stainless steel</h3>
    <p>
      How laser powder bed fusion (LPBF) 316L behaves once it is taken to temperature, and
      how much of that behaviour is inherited from the way it was printed.
    </p>
    <ul class="interests">
      <li>
        <strong>High-temperature deformation.</strong> Systematic investigation of the
        mechanical behaviour of LPBF-fabricated 316L stainless steel at an elevated
        temperature of 850&nbsp;&deg;C.
      </li>
      <li>
        <strong>Anisotropy and build orientation.</strong> Uniaxial tensile response
        compared along vertical (parallel to build) and horizontal (perpendicular to build)
        orientations, to isolate the effect of build direction on mechanical performance.
      </li>
      <li>
        <strong>Strain-rate sensitivity.</strong> Response across multiple strain rates,
        revealing a transition from strain softening at lower rates to strain hardening at
        higher rates.
      </li>
      <li>
        <strong>Microstructural mechanisms.</strong> Deformation shifts from dislocation
        slip and twinning at room temperature to dynamic recrystallisation at elevated
        temperature.
      </li>
    </ul>

    <div class="figs">
      <figure>
        <img src="images/lpbf-01.jpg" alt="Microstructure of LPBF 316L stainless steel." loading="lazy">
        <figcaption>LPBF 316L microstructure.</figcaption>
      </figure>
      <figure>
        <img src="images/lpbf-02.jpg" alt="Tensile response at 850 degrees Celsius across strain rates." loading="lazy">
        <figcaption>Tensile response at 850&nbsp;&deg;C across strain rates.</figcaption>
      </figure>
      <figure>
        <img src="images/lpbf-03.jpg" alt="Vertical versus horizontal build orientation." loading="lazy">
        <figcaption>Vertical vs. horizontal build orientation.</figcaption>
      </figure>
    </div>

    <p>
      Full paper:
      <a href="https://doi.org/10.1016/j.addma.2026.105115">Orientation and strain-rate
      effects on high-temperature plasticity of 316L stainless steel fabricated by laser
      powder bed fusion</a>.
    </p>
'''

PUBLICATIONS = '''
    <h2>Publications</h2>

    <ol class="pubs">
      <li>
        <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=Wm7uCdcAAAAJ&amp;citation_for_view=Wm7uCdcAAAAJ:u5HHmVD_uO8C">Orientation
        and Strain-Rate Effects on High-Temperature Plasticity of 316 L Stainless Steel
        Fabricated by Laser Powder Bed Fusion</a>, <em>Additive Manufacturing</em>.
        [<a href="https://doi.org/10.1016/j.addma.2026.105115">https://doi.org/10.1016/j.addma.2026.105115</a>]
      </li>
      <li>
        <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=Wm7uCdcAAAAJ&amp;citation_for_view=Wm7uCdcAAAAJ:d1gkVwhDpl0C">Studying
        Creep-Fatigue Interaction of Nickel-Based Superalloys using Crystal Plasticity and
        Entropy-Based Life Prediction Model</a>, preprint.
        [<a href="https://arxiv.org/abs/2605.23342">https://arxiv.org/abs/2605.23342</a>]
      </li>
    </ol>

    <p>
      A complete and up-to-date list is available on
      <a href="https://scholar.google.com/citations?user=Wm7uCdcAAAAJ&amp;hl=en">Google Scholar</a>.
    </p>

    <h2 style="margin-top:36px">Conference presentations</h2>

    <ol class="pubs">
      <li>
        S. K. Shaw, R. Paliwal, S. Chatterjee, A. Alankar.
        <em>Modeling of creep&ndash;fatigue interaction and life prediction of a turbine
        blade made of single-crystal nickel superalloys</em>.
        17th World Congress on Computational Mechanics (WCCM) and 10th European
        Congress on Computational Methods in Applied Sciences and Engineering
        (ECCOMAS), Munich, Germany, 22 July 2026.
      </li>
    </ol>
'''

TEACHING = '''
    <h2>Teaching</h2>
    <p>
      <strong>Teaching Assistantship:</strong> facilitated learning, graded assignments and
      supported faculty across the following undergraduate and postgraduate courses.
    </p>

    <ol class="courses">
      <li><span class="code">APL410</span> &mdash; Multiscale Modelling</li>
      <li><span class="code">AML8200</span> &mdash; Plasticity</li>
      <li><span class="code">APL380</span> &mdash; Biomechanics</li>
      <li><span class="code">APL103</span> &mdash; Experimental Methods</li>
      <li><span class="code">APL100</span> &mdash; Engineering Mechanics</li>
    </ol>
'''

SOFTWARE = '''
    <h2>Software</h2>
    <p>
      Model implementations and the supporting data behind the papers are released openly.
      Everything runs on the MOOSE framework unless noted otherwise.
    </p>

    <h3>CFI-CPFEM</h3>
    <p>
      Dislocation density-based crystal plasticity finite element model for
      creep&ndash;fatigue interaction in single-crystal nickel superalloys, with the input
      decks and supporting data for the accompanying paper.
    </p>
    <p><a href="https://github.com/SKS-CP/CFI-CPFEM">https://github.com/SKS-CP/CFI-CPFEM</a></p>

    <p>All repositories: <a href="https://github.com/SKS-CP">https://github.com/SKS-CP</a></p>
'''

CONTACT = '''
    <h2>Contact</h2>

    <p>Research Scholar Room 4A/14, Block IV</p>
    <p>Dept. of Applied Mechanics, IIT Delhi</p>
    <p>Hauz Khas, New Delhi 110016, India.</p>
    <p>Email: <a href="mailto:amz228601@iitd.ac.in">amz228601@iitd.ac.in</a></p>
    <p>Contact: <a href="tel:+917001931050">+91-7001931050</a></p>

    <p class="inline-links">
      <a href="https://scholar.google.com/citations?user=Wm7uCdcAAAAJ&amp;hl=en">Google Scholar</a>
      <a href="https://www.linkedin.com/in/santosh-shaw-a13744275/">Linkedin</a>
      <a href="https://github.com/SKS-CP">Github</a>
    </p>

    <iframe class="map" title="Map of the Department of Applied Mechanics, IIT Delhi" loading="lazy"
      src="https://www.openstreetmap.org/export/embed.html?bbox=77.1877%2C28.5444%2C77.1957%2C28.5484&amp;layer=mapnik&amp;marker=28.5463655%2C77.1917207"></iframe>
    <p><a href="https://www.openstreetmap.org/?mlat=28.5463655&amp;mlon=77.1917207#map=17/28.54637/77.19172">Open larger map</a></p>
'''

PAGES = [
    ("index.html", "Home", "Santosh Kumar Shaw — Applied Mechanics, IIT Delhi",
     "Research Scholar at the Department of Applied Mechanics, IIT Delhi, working on "
     "crystal plasticity and creep-fatigue interaction in nickel superalloys.", HOME),
    ("bio-sketch.html", "Bio-sketch", "Bio-sketch — Santosh Kumar Shaw",
     "Education, research summary and technical skills.", BIO),
    ("research.html", "Research", "Research — Santosh Kumar Shaw",
     "Creep-fatigue interaction in nickel superalloy turbine blades and high-temperature "
     "plasticity of LPBF 316L stainless steel.", RESEARCH),
    ("publications.html", "Publications", "Publications — Santosh Kumar Shaw",
     "Journal articles and preprints.", PUBLICATIONS),
    ("teaching.html", "Teaching", "Teaching — Santosh Kumar Shaw",
     "Courses supported as a teaching assistant at IIT Delhi.", TEACHING),
    ("software.html", "Software", "Software — Santosh Kumar Shaw",
     "Open crystal plasticity finite element models and supporting data.", SOFTWARE),
    ("contact.html", "Contact", "Contact — Santosh Kumar Shaw",
     "Office address, email and phone at the Department of Applied Mechanics, IIT Delhi.",
     CONTACT),
]


def plain_text(fragment):
    """Strip tags and collapse whitespace, for the search index."""
    text = re.sub(r"<[^>]+>", " ", fragment)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


index = []
for slug, nav_label, title, desc, body in PAGES:
    with open(os.path.join(OUT, slug), "w") as f:
        f.write(page(slug, title, desc, body))
    index.append({"url": slug, "title": nav_label, "text": plain_text(body)})
    print("wrote", slug)

with open(os.path.join(OUT, "assets", "search-index.js"), "w") as f:
    f.write("window.SEARCH_INDEX = " + json.dumps(index, indent=1) + ";\n")
print("wrote assets/search-index.js")
