"""Generate the PremLabs DSA tutorial site.  Run from the repo root:  python3 tools/build.py"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from content import TOPICS  # noqa: E402

SITE = "https://premlabs.github.io"
BASE = SITE + "/datastructure/"
UPDATED = "2026-11-16"
AUTHOR = {"@type": "Person", "name": "Prem Sarojanand", "url": SITE + "/",
          "jobTitle": "Senior Software Engineer"}
PUBLISHER = {"@type": "Organization", "name": "PremLabs", "url": SITE + "/",
             "logo": {"@type": "ImageObject", "url": BASE + "assets/og.png"}}
LANGS = [("py", "Python"), ("java", "Java"), ("js", "JavaScript")]
VERSION = "2"  # cache-buster for css/js

ANALYTICS = """  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-TLJBPCN6');</script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-MZDBK7RPZJ"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-MZDBK7RPZJ');</script>"""

esc = html.escape
strip = lambda s: re.sub(r"<[^>]+>", "", s).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def head(title, desc, url, prefix, ld, og_type="article"):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="author" content="Prem Sarojanand">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#fbfbfd" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="PremLabs">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}assets/og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{BASE}assets/og.png">
  <link rel="icon" href="{prefix}assets/icon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}assets/site.css?v={VERSION}">
  <script src="{prefix}assets/viz.js?v={VERSION}" defer></script>
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{ANALYTICS}
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TLJBPCN6" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="nav-in">
  <a class="brand" href="{prefix}">PremLabs <span>DSA</span></a>
  <nav class="nav-links" aria-label="Main">
    <a href="{prefix}#tutorials">Tutorials</a>
    <a class="opt" href="{prefix}sorting-algorithms/">Visualizer</a>
    <a class="opt" href="https://github.com/PremLabs/datastructure">GitHub</a>
    <a class="pill-link" href="{SITE}/">Hire me</a>
  </nav>
</div></header>
"""


FOOT = f"""<footer><div class="foot">
  <span>© 2026 PremLabs · Free data structures and algorithms tutorials by <a href="{SITE}/">Prem Sarojanand</a></span>
  <span><a href="https://www.youtube.com/@PremLabs-s05w" rel="me">YouTube</a> · <a href="https://www.instagram.com/tech.coders/" rel="me">Instagram</a> · <a href="https://github.com/PremLabs" rel="me">GitHub</a> · <a href="{BASE}sitemap.xml">Sitemap</a></span>
</div></footer>
</body>
</html>
"""


def code_block(slug):
    files = {k: (ROOT / "tools" / "code" / f"{slug}.{k}").read_text().rstrip() for k, _ in LANGS}
    tabs = "".join(f'<button type="button" role="tab" data-lang="{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{name}</button>'
                   for i, (k, name) in enumerate(LANGS))
    pres = "".join(f'<pre data-lang="{k}" role="tabpanel" aria-label="{name} code"{"" if i == 0 else " hidden"}><code>{esc(files[k])}</code></pre>'
                   for i, (k, name) in enumerate(LANGS))
    return f'<div class="code"><div class="tabs" role="tablist" aria-label="Language">{tabs}<button type="button" class="copy">Copy</button></div>{pres}</div>', files


def ops_table(ops):
    rows = "".join(f"<tr><td>{a}</td><td><code>{b}</code></td><td><code>{c}</code></td><td>{d}</td></tr>" for a, b, c, d in ops)
    return ('<div class="tablewrap"><table><thead><tr><th>Operation</th><th>Average</th><th>Worst</th><th>Notes</th></tr></thead>'
            f"<tbody>{rows}</tbody></table></div>")


def sidebar(current):
    out, group = [], None
    for t in TOPICS:
        if t["group"] != group:
            if group is not None:
                out.append("</ol>")
            group = t["group"]
            out.append(f"<h2>{esc(group)}</h2><ol>" if not out else f'<h2 style="margin-top:1.2rem">{esc(group)}</h2><ol>')
        cur = ' aria-current="page"' if t["slug"] == current else ""
        out.append(f'<li><a href="../{t["slug"]}/"{cur}>{esc(t["title"])}</a></li>')
    out.append("</ol>")
    return '<nav class="side" aria-label="All tutorials">' + "".join(out) + "</nav>"


def page(i, t):
    url = f"{BASE}{t['slug']}/"
    code_html, files = code_block(t["slug"])
    prev_t = TOPICS[i - 1] if i > 0 else None
    next_t = TOPICS[i + 1] if i < len(TOPICS) - 1 else None
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": ["TechArticle", "LearningResource"], "@id": url + "#article", "headline": t["seo_title"],
         "name": t["title"], "description": t["description"], "url": url, "mainEntityOfPage": url,
         "image": BASE + "assets/og.png", "author": AUTHOR, "publisher": PUBLISHER,
         "datePublished": UPDATED, "dateModified": UPDATED, "inLanguage": "en",
         "learningResourceType": "Tutorial", "educationalLevel": t["facts"][0][1],
         "teaches": t["title"], "about": {"@type": "Thing", "name": t["title"]},
         "isAccessibleForFree": True, "programmingLanguage": ["Python", "Java", "JavaScript"],
         "isPartOf": {"@id": BASE + "#course"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "PremLabs", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Data Structures & Algorithms", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": t["title"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in t["faq"]]},
    ]}
    facts = "".join(f"<li>{esc(k)}: <b>{esc(v)}</b></li>" for k, v in t["facts"])
    parts = [head(t["seo_title"] + " | PremLabs", t["description"], url, "../", ld),
             '<div class="layout">', sidebar(t["slug"]), '<article id="main">',
             f'<p class="crumbs"><a href="../">Data Structures &amp; Algorithms</a> › {esc(t["group"])}</p>',
             f'<h1>{esc(t["title"])}</h1>', f'<p class="lede">{t["lede"]}</p>', f'<ul class="facts">{facts}</ul>',
             t["intro"],
             f'<div data-viz="{t["viz"]}" aria-label="Interactive {esc(t["title"])} visualizer"><noscript><p class="note">The interactive visualizer needs JavaScript. Everything else on this page works without it.</p></noscript></div>',
             t["body"]]
    if t["ops"]:
        parts += ['<h2 id="complexity">Time complexity</h2>', ops_table(t["ops"])]
    parts += [f'<h2 id="code">{esc(t["title"])} in Python, Java and JavaScript</h2>',
              '<p>Every sample below runs as is and prints the results shown in its comments. Switch language with the tabs; your choice is remembered on every page.</p>',
              code_html]
    if t["uses"]:
        a_title, a_items, b_title, b_items = t["uses"]
        parts += ['<h2 id="when">When to use it</h2>', f"<h3>{a_title}</h3><ul>" + "".join(f"<li>{x}</li>" for x in a_items) + "</ul>",
                  f"<h3>{b_title}</h3><ul>" + "".join(f"<li>{x}</li>" for x in b_items) + "</ul>"]
    parts += ['<h2 id="mistakes">Common mistakes</h2><ul>' + "".join(f"<li>{m}</li>" for m in t["mistakes"]) + "</ul>",
              '<h2 id="interview">Interview questions</h2><p>Classic problems built on this topic, with the approach to each. Try them yourself before opening the hint.</p>',
              "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["interview"]),
              '<h2 id="faq">Frequently asked questions</h2>',
              "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in t["faq"])]
    pager = '<nav class="pager" aria-label="Next and previous tutorials">'
    if prev_t:
        pager += f'<a href="../{prev_t["slug"]}/" rel="prev"><small>Previous</small>{esc(prev_t["title"])}</a>'
    if next_t:
        pager += f'<a class="next" href="../{next_t["slug"]}/" rel="next"><small>Next</small>{esc(next_t["title"])}</a>'
    pager += "</nav>"
    parts += [pager,
              f'<aside class="hire"><p><b>Written by Prem Sarojanand</b>Senior software engineer with 13+ years of Java, Node.js and Python experience. Open to remote and freelance work.</p><a class="btn primary" href="{SITE}/#contact">Work with me</a></aside>',
              "</article></div>", FOOT]
    out = ROOT / t["slug"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(parts))
    return files


def hub():
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": BASE + "#site", "name": "PremLabs Data Structures & Algorithms", "url": BASE, "publisher": PUBLISHER, "inLanguage": "en"},
        {"@type": "Course", "@id": BASE + "#course", "name": "Data Structures and Algorithms, Visually",
         "description": "A free, interactive course covering Big-O, arrays, linked lists, stacks, queues, hash tables, trees, heaps, tries, graphs, binary search and sorting, with code in Python, Java and JavaScript.",
         "url": BASE, "provider": PUBLISHER, "author": AUTHOR, "inLanguage": "en", "isAccessibleForFree": True,
         "educationalLevel": "Beginner to intermediate",
         "offers": {"@type": "Offer", "price": 0, "priceCurrency": "USD", "category": "Free"},
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": "PT2H"},
         "hasPart": [{"@type": "LearningResource", "name": t["title"], "url": f"{BASE}{t['slug']}/"} for t in TOPICS]},
        {"@type": "ItemList", "name": "Tutorials", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f"{BASE}{t['slug']}/", "name": t["title"]} for i, t in enumerate(TOPICS)]},
    ]}
    title = "Data Structures and Algorithms Tutorials with Visualizations | PremLabs"
    desc = ("Free interactive data structures and algorithms tutorials with animated visualizers "
            "and tested code in Python, Java and JavaScript. From Big-O to graphs.")
    groups = []
    for t in TOPICS:
        if not groups or groups[-1][0] != t["group"]:
            groups.append((t["group"], []))
        groups[-1][1].append(t)
    n = 0
    body = [head(title, desc, BASE, "", ld, "website"),
            '<main id="main">',
            '<section class="hero"><p class="eyebrow">Free · Interactive · Python, Java &amp; JavaScript</p>',
            '<h1>Data structures,<br>made visible.</h1>',
            '<p class="lede">Thirteen tutorials that explain each structure in plain language, let you operate it step by step, and give you tested code in three languages. Built for interview preparation and for understanding what your code is actually doing.</p>',
            '<div class="actions"><a class="btn primary" href="big-o/">Start with Big-O</a><a class="btn" href="sorting-algorithms/">Open the sorting visualizer</a></div></section>',
            '<div class="hub" id="tutorials">',
            '<label for="filter" class="eyebrow" style="display:block">Find a topic</label>',
            '<input id="filter" class="search" type="search" placeholder="Try “heap”, “O(log n)” or “BFS”" autocomplete="off">',
            '<p id="empty" class="empty" hidden>No tutorial matches that search.</p>']
    for name, items in groups:
        body.append(f'<section data-group><h2>{esc(name)}</h2><ul class="cards">')
        for t in items:
            n += 1
            tags = "".join(f'<span class="tag">{esc(x)}</span>' for x in t["tags"])
            search = " ".join([t["title"], t["blurb"], name, *t["tags"]]).lower()
            body.append(f'<li data-search="{esc(search)}"><a class="card" href="{t["slug"]}/"><span class="num">{n:02d}</span>'
                        f'<h3>{esc(t["title"])}</h3><p>{esc(t["blurb"])}</p><span class="meta">{tags}</span></a></li>')
        body.append("</ul></section>")
    body += ['<section><h2>How each tutorial is built</h2><p class="sub">The same structure on every page, so you always know where to look.</p>',
             '<ul class="cards">',
             '<li><div class="card"><h3>Plain explanation</h3><p>What the structure is, with an everyday analogy, before any code.</p></div></li>',
             '<li><div class="card"><h3>Interactive visual</h3><p>Insert, delete, search and traverse yourself. Each step is narrated.</p></div></li>',
             '<li><div class="card"><h3>Tested code</h3><p>Python, Java and JavaScript implementations that run exactly as shown.</p></div></li>',
             '<li><div class="card"><h3>Interview practice</h3><p>Complexity tables, common mistakes and classic interview questions with hints.</p></div></li>',
             "</ul></section></div></main>", FOOT]
    (ROOT / "index.html").write_text("\n".join(body))


def sitemap():
    urls = [BASE] + [f"{BASE}{t['slug']}/" for t in TOPICS]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        xml.append(f"  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod></url>")
    xml.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(xml) + "\n")


if __name__ == "__main__":
    for i, t in enumerate(TOPICS):
        page(i, t)
    hub()
    sitemap()
    print(f"built {len(TOPICS)} tutorials + hub + sitemap")
