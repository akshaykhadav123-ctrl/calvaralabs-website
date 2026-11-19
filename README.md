# calvaralabs.com

Website of Calvara Labs & Minerals: hydrated lime (grades 80–95 % Ca(OH)₂) and hydroxyapatite, Jodhpur, India.

- `docs/` is the live website served by GitHub Pages at https://calvaralabs.com (static HTML, no build step on GitHub).
- `source/` holds the generator: `python3 source/build.py live` writes the site to `source/dist/`; copy that into `docs/` to publish.
  - Page text, grades, contact details and the rotating announcement messages (`ANNOUNCEMENTS`) are in `source/build.py`.
  - Styles: `source/src/assets/site.css`. Photos: `source/src/photos/`. Logo files: `source/src/brand/`.
- Brochures: PDFs in `source/src/brochures/`, listed in `BROCHURES` in `source/build.py` (hydroxyapatite brochure: set its `file` when ready).
- Contact form posts to FormSubmit (sales@calvaralabs.com). WhatsApp buttons open +91 98927 27068.
