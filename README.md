# Shri Padmalaya Tours & Travels

A responsive travel website with a cinematic ocean hero, animated section reveals, hover-driven travel experiences, destination details, English/Marathi support, and WhatsApp trip enquiries.

## Run locally

Requires Node.js. No dependency installation is needed to serve the website.

```sh
node design-preview/serve.cjs
```

Open http://127.0.0.1:4173/. To use another port:

```sh
node design-preview/serve.cjs --port 4174
```

The full animated experience is the default. The muted hero video starts automatically and loops without an on-image Play/Pause button. Visitors can use the footer's **Reduce motion** control to switch motion off and **Enable animations** to restore it; that choice is saved on their device. The `?motion=reduced` and `?motion=full` URL options provide explicit overrides. Video playback pauses while the page is hidden or the video is offscreen, then resumes when visible.

## Editing and building

The deployable website is `index.html` and `assets/`. Source files for the current design are in `.design-tools/aventiora-site.template.html`, `.design-tools/aventiora-site.css`, and `.design-tools/aventiora-site.js`.

After changing those source files, rebuild using Python 3:

```sh
python .design-tools/build-aventiora-site.py
```

The build updates the generated HTML, CSS, JavaScript, and asset cache identifiers. A local backup of the previous HTML is kept in the ignored `backups/` directory.

Destination content, translations, and contact configuration are in `assets/site-data.js`. Enquiries prepare a WhatsApp message for the customer to review and send; they are not sent automatically.

## Hosting

Deploy `index.html` and `assets/` together to a static web host. No server-side application or build service is required. The included Node.js server is for local previews.

## Media and dependencies

Photographer and film credits, source links, and license links are recorded in `assets/travel/credits.json`. Entries marked as archived alternatives are not loaded by the website. Font licenses are in `assets/fonts/`, and vendor notices are in `assets/vendor/THIRD-PARTY-NOTICES.txt`.

Local design experiments, raw recordings, backups, and QA artifacts are excluded from version control.
