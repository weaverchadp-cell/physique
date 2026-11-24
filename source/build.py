"""Rebuild the app at the repo root from source/: python3 source/build.py"""
import pathlib, time
here = pathlib.Path(__file__).resolve().parent
out = here.parent
app = (here / 'app.html').read_text()
head_part, body_part = app.split('<div id="app">', 1)
body_part = '<div id="app">' + body_part
version = time.strftime('%Y%m%d%H%M')
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Physique">
<meta name="application-name" content="Physique">
<meta name="format-detection" content="telephone=no">
<meta name="description" content="Push, Pull, Legs workout tracker">
<meta name="theme-color" content="#F3F4F8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#08090D" media="(prefers-color-scheme: dark)">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head_part.strip()}
</head>
<body>
{body_part.strip()}
</body>
</html>
'''
(out / 'index.html').write_text(page)
(out / 'manifest.webmanifest').write_text((here / 'manifest.webmanifest').read_text())
(out / 'sw.js').write_text((here / 'sw.js').read_text().replace('__VERSION__', version))
(out / '.nojekyll').write_text('')
print('built', version)
