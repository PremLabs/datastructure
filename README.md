# PremLabs DSA Playground

A zero-build, GitHub Pages-ready interactive Python DSA learning page.

## Features

- Step-by-step visualizations for Bubble Sort, Selection Sort, Insertion Sort, and Merge Sort
- Play, pause, step, reset, randomize, array-size, and speed controls
- Comparison and swap/shift counters, progress, Python examples, and time/space complexity
- Google Analytics 4 event tracking hooks
- Public visitor badge in the footer

## Publish with GitHub Pages

1. Open **Settings → Pages** in this repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**, then save.
4. Wait for the Pages deployment to finish. The site URL is normally `https://premlabs.github.io/datastructure/`.

No build command or package installation is required; the site is a static `index.html`.

## Connect your existing Google Analytics 4 property

1. In Google Analytics, open **Admin → Data streams**, select the web stream for this site, and copy its Measurement ID (format: `G-XXXXXXXXXX`).
2. Edit `index.html` and replace `G-XXXXXXXXXX` in `GA_MEASUREMENT_ID` with your actual ID.
3. Commit the change and wait for Pages to redeploy.
4. Verify events in **Reports → Realtime** or **Admin → DebugView**. The page tracks standard page views plus `select_algorithm`, `play_visualization`, `step_visualization`, and `randomize_array` when analytics is configured.

The Measurement ID was not supplied with this request, so the placeholder is intentionally left in place. Analytics will not send data until you replace it. Make sure your site's privacy notice and consent setup meet the requirements applicable to your audience.

## Public visit counter

The footer uses a third-party visitor badge service with the key `PremLabs.datastructure`. It is separate from Google Analytics and shows a public count image. The badge service controls its own counting, availability, and privacy practices; the number may not match GA4 users or sessions.

## Local preview

Open `index.html` in a browser. Since this is a static page, no local development server is needed.
