# Santosh Kumar Shaw — academic website

A static seven-page site laid out in the style of the Applied Mechanics faculty pages:
dark top navigation, blue title banner, single white content column. No framework and no
build step — plain HTML and one stylesheet, so GitHub Pages serves it as-is.

```
index.html          Home — about me, interests, contact
bio-sketch.html     Bio-sketch — education, research summary, skills
research.html       Research — the two research threads, with figures
publications.html   Publications
teaching.html       Teaching assistantship
software.html       Code and data releases
contact.html        Address, phone, map
style.css           All styling
assets/             Small helper script and placeholder graphic
images/             Your photo and figures (see images/README.md)
files/              Your CV (see files/README.md)
```

## 1. Fill in the three placeholders first

1. Open `bio-sketch.html` and replace the two italic `[Add your ... here]` lines with your
   actual Master's and Bachelor's details. They are visible on the live page until you do.
2. Save your photo as `images/photo.jpg`.
3. Save your CV as `files/cv.pdf`.

## 2. Put it online

1. Go to GitHub and create a **new empty repository** named exactly `SKS-CP.github.io`.
   Do not add a README, .gitignore or licence — leave it completely empty.
2. Open a terminal in this folder (the one containing `index.html`).
3. Run these commands one at a time:
   ```bash
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/SKS-CP/SKS-CP.github.io.git
   git push -u origin main
   ```
4. On GitHub, open the repository → **Settings** → **Pages**.
5. Under "Build and deployment", set Source to **Deploy from a branch**, branch **main**,
   folder **/ (root)**, then click **Save**.
6. Wait about a minute, then open **https://SKS-CP.github.io** — the site is live.

If you prefer a different repository name, say `website`, everything above still works;
the address becomes `https://SKS-CP.github.io/website/` instead.

## 3. Add your figures

1. Download each image from your Google Site (right-click → Save image as).
2. Rename them to the filenames listed in `images/README.md`.
3. Drop them into the `images/` folder.
4. Commit and push:
   ```bash
   git add images
   git commit -m "Add figures"
   git push
   ```

## 4. Update the site later

1. Edit the relevant `.html` file in any text editor. The text you want to change is
   plainly visible in the middle of the file.
2. To add a publication, copy one `<li>` block in `publications.html` and change the
   title and links. The `(1)` `(2)` numbering is automatic.
3. To add a course, copy one `<li>` line in `teaching.html`.
4. To add a whole new page, the fastest route is to copy an existing page, replace the
   content between `<main>` and `</main>`, then add one `<li>` to the navigation list in
   every page.
5. Save, then run:
   ```bash
   git add .
   git commit -m "Update publications"
   git push
   ```
6. The live site updates within a minute or so.

## 5. Point your own domain at it (optional)

1. Buy a domain, for example `santoshshaw.in`.
2. At your registrar, add four A records pointing to `185.199.108.153`,
   `185.199.109.153`, `185.199.110.153` and `185.199.111.153`.
3. In the repository, Settings → Pages → Custom domain, enter the domain and save.
4. Tick **Enforce HTTPS** once the certificate has been issued.

## Notes

- `assets/build_pages.py` regenerates all seven pages from one shared template, which is
  what keeps the navigation identical everywhere. If you start editing the pages by hand,
  do not run it again — it overwrites them. You can delete it once you are happy.
- `assets/site.js` swaps in a placeholder for any image that has not been added yet.
- The colours are set once at the top of `style.css` (`--banner` is the blue, `--bar` the
  dark navigation, `--link` the red of the links). Change them there and every page
  follows.
