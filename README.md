# Physique

A Push / Pull / Legs workout tracker that installs to the iPhone home screen. It logs sets, extra sets and drop sets, works out volume (sets × reps × weight), and charts each exercise's weight over time.

**Open it:** https://weaverchadp-cell.github.io/physique/ in Safari, then Share → Add to Home Screen.

Workout data is stored on the phone, not in this repository. Back it up from Settings in the app.

## Files
- `index.html`, `manifest.webmanifest`, `sw.js`, `icons/`: the published app (built, don't edit by hand).
- `source/app.html`: the app itself (styles, screens and logic in one file). Edit this, then run `python3 source/build.py` to rebuild the files above.
