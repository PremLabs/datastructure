# PremLabs DSA — Data structures, made visible

Free, interactive data structures and algorithms tutorials: **https://premlabs.github.io/datastructure/**

Thirteen tutorials, each with a plain-language explanation, an interactive visualizer, a complexity table, tested code in **Python, Java and JavaScript**, common mistakes, interview questions and an FAQ.

| # | Tutorial | Visualizer |
|---|----------|------------|
| 1 | [Big-O Notation](https://premlabs.github.io/datastructure/big-o/) | Growth-rate slider |
| 2 | [Arrays](https://premlabs.github.io/datastructure/arrays/) | Insert / delete / access / search with shifting |
| 3 | [Linked Lists](https://premlabs.github.io/datastructure/linked-list/) | Nodes and pointers |
| 4 | [Stacks](https://premlabs.github.io/datastructure/stack/) | Push / pop / peek |
| 5 | [Queues](https://premlabs.github.io/datastructure/queue/) | Enqueue / dequeue |
| 6 | [Hash Tables](https://premlabs.github.io/datastructure/hash-table/) | Hashing, buckets and collisions |
| 7 | [Binary Trees & Traversals](https://premlabs.github.io/datastructure/binary-tree/) | In-, pre-, post- and level-order |
| 8 | [Binary Search Trees](https://premlabs.github.io/datastructure/binary-search-tree/) | Insert / search / delete, unbalanced case |
| 9 | [Heaps & Priority Queues](https://premlabs.github.io/datastructure/heap/) | Sift up / down in tree and array views |
| 10 | [Tries](https://premlabs.github.io/datastructure/trie/) | Insert, search, prefix autocomplete |
| 11 | [Graphs: BFS & DFS](https://premlabs.github.io/datastructure/graph/) | Animated BFS and DFS |
| 12 | [Binary Search](https://premlabs.github.io/datastructure/binary-search/) | lo / mid / hi pointers |
| 13 | [Sorting Algorithms](https://premlabs.github.io/datastructure/sorting-algorithms/) | Bubble, selection, insertion, merge, quick |

## How the site is built

Static HTML, no framework, no build step needed to serve it.

```
assets/site.css      shared styles (light/dark, reduced motion, high contrast)
assets/viz.js        all visualizers, code tabs, search (no dependencies)
tools/content.py     tutorial text
tools/code/          runnable code samples: <slug>.py / .java / .js
tools/build.py       generates <slug>/index.html, index.html and sitemap.xml
```

To change a tutorial, edit `tools/content.py` or a file in `tools/code/`, then run:

```bash
python3 tools/build.py
```

Every code sample runs as-is: `python3 tools/code/heap.py`, `node tools/code/heap.js`, or copy the `.java` file to its class name and `javac`/`java` it.

## SEO

Each page has a unique title and description, canonical URL, Open Graph/Twitter cards, and JSON-LD (`TechArticle`, `BreadcrumbList`, `FAQPage`; the hub has `Course` and `ItemList`). `sitemap.xml` is referenced from `https://premlabs.github.io/robots.txt`.

Analytics: Google Tag Manager `GTM-TLJBPCN6` and GA4 `G-MZDBK7RPZJ`.

## Author

[Prem Sarojanand](https://premlabs.github.io/) — senior Java, Node.js and Python engineer, open to remote and freelance work.
