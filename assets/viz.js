/* PremLabs DSA — interactive visualizers. No dependencies.
   Every operation is interruptible: starting a new one cancels the one in flight. */
(() => {
'use strict';
const SVGNS = 'http://www.w3.org/2000/svg';
const CANCEL = Symbol('cancel');
const h = (tag, attrs = {}, ...kids) => {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') e.className = v;
    else if (k === 'text') e.textContent = v;
    else if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
    else e.setAttribute(k, v);
  }
  for (const c of kids.flat()) if (c != null) e.append(c);
  return e;
};
const s = (tag, attrs = {}, text) => {
  const e = document.createElementNS(SVGNS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  if (text != null) e.textContent = text;
  return e;
};
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));
const num = (input, fallback = 0) => { const v = parseInt(input.value, 10); return Number.isFinite(v) ? v : fallback; };
const rand = (lo, hi) => Math.floor(Math.random() * (hi - lo + 1)) + lo;

function frame(root) {
  root.classList.add('viz');
  root.textContent = '';
  const controls = h('div', { class: 'viz-controls' });
  const stage = h('div', { class: 'viz-stage' });
  const log = h('p', { class: 'viz-log', 'aria-live': 'polite' });
  root.append(controls, stage, log);
  let token = 0;
  const speeds = [['1×', 600], ['2×', 300], ['½×', 1100]];
  let sp = 0;
  const api = {
    controls, stage,
    say: t => { log.textContent = t; },
    wait(mult = 1) {
      const mine = token;
      return new Promise((res, rej) => setTimeout(() => (mine === token ? res() : rej(CANCEL)), speeds[sp][1] * mult));
    },
    cancel() { token++; },
    run(fn) { token++; Promise.resolve().then(fn).catch(e => { if (e !== CANCEL) throw e; }); },
    btn(label, fn, primary) {
      const b = h('button', { type: 'button', class: 'btn' + (primary ? ' primary' : ''), text: label, onclick: () => api.run(fn) });
      controls.append(b); return b;
    },
    input(label, value, attrs = {}) {
      const i = h('input', { value, inputmode: attrs.type === 'number' ? 'numeric' : 'text', ...attrs });
      controls.append(h('label', { class: 'field' }, h('span', { text: label }), i)); return i;
    },
    select(label, options) {
      const el = h('select', {}, options.map(([v, t]) => h('option', { value: v, text: t })));
      controls.append(h('label', { class: 'field' }, h('span', { text: label }), el)); return el;
    },
    speed() {
      const b = h('button', { type: 'button', class: 'btn', text: 'Speed 1×', 'aria-label': 'Change animation speed',
        onclick: () => { sp = (sp + 1) % speeds.length; b.textContent = 'Speed ' + speeds[sp][0]; } });
      controls.append(b);
    },
    delay: () => speeds[sp][1],
  };
  return api;
}

function cells(items, { marks = {}, ptr = null, index = true, vertical = false } = {}) {
  const row = h('div', { class: 'cells' + (vertical ? ' vertical' : '') });
  items.forEach((v, i) => row.append(h('div', { class: 'cellwrap' },
    ptr ? h('span', { class: 'ptr', text: ptr[i] || '' }) : null,
    h('div', { class: 'cell ' + (v == null ? 'empty ' : '') + (marks[i] || ''), text: v == null ? '' : String(v) }),
    index ? h('span', { class: 'idx', text: String(i) }) : null)));
  return row;
}
const legend = () => h('div', { class: 'legend' },
  h('span', {}, h('i', { class: 'a' }), 'Looking at'), h('span', {}, h('i', { class: 'f' }), 'Result'), h('span', {}, h('i', { class: 'v' }), 'Visited'));

/* Tree drawing. Binary trees use in-order x positions; n-ary trees centre parents over leaves. */
function treeSvg(root, { kids, label, cls = () => '', binary = true }) {
  const pos = new Map(); let col = 0, depthMax = 0;
  const place = (n, d) => {
    if (!n) return;
    depthMax = Math.max(depthMax, d);
    if (binary) { const [l, r] = kids(n); place(l, d + 1); pos.set(n, { x: col++, y: d }); place(r, d + 1); }
    else {
      const ks = kids(n);
      if (!ks.length) pos.set(n, { x: col++, y: d });
      else { ks.forEach(k => place(k, d + 1)); pos.set(n, { x: (pos.get(ks[0]).x + pos.get(ks[ks.length - 1]).x) / 2, y: d }); }
    }
  };
  place(root, 0);
  const GX = 46, GY = 62, R = 17, W = Math.max(col, 1) * GX + 10, H = depthMax * GY + R * 2 + 12;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img', 'aria-label': 'Tree diagram' });
  svg.style.maxWidth = Math.max(W * 1.25, 220) + 'px';
  const xy = n => { const p = pos.get(n); return [p.x * GX + GX / 2 + 5, p.y * GY + R + 6]; };
  const edges = s('g'), nodes = s('g');
  for (const n of pos.keys()) {
    const [x, y] = xy(n);
    for (const k of kids(n)) if (k) { const [kx, ky] = xy(k); edges.append(s('line', { x1: x, y1: y, x2: kx, y2: ky, class: cls(k).includes('hidden') ? 'hidden' : '' })); }
    const g = s('g', { class: cls(n) });
    g.append(s('circle', { cx: x, cy: y, r: R }), s('text', { x, y }, label(n)));
    nodes.append(g);
  }
  svg.append(edges, nodes);
  return svg;
}

const V = {};

/* ---------- Array ---------- */
V.array = root => {
  const f = frame(root); let a = [12, 45, 7, 23, 56]; const CAP = 9;
  const val = f.input('Value', '30', { type: 'number' }), idx = f.input('Index', '2', { type: 'number', min: 0 });
  const draw = (arr, marks = {}) => f.stage.replaceChildren(cells(arr, { marks }), legend());
  f.btn('Insert', async () => {
    if (a.length >= CAP) { draw(a); return f.say(`The array is full (capacity ${CAP}). A dynamic array would now allocate a bigger block and copy everything across.`); }
    const v = num(val), i = clamp(num(idx), 0, a.length), t = a.concat([null]);
    a = a.slice(0, i).concat([v], a.slice(i));
    draw(t); f.say(`Insert ${v} at index ${i}. Everything from index ${i} onward has to move one slot right first.`); await f.wait();
    for (let j = t.length - 1; j > i; j--) { t[j] = t[j - 1]; t[j - 1] = null; draw(t, { [j]: 'active' }); f.say(`Shift ${t[j]} from index ${j - 1} to index ${j}.`); await f.wait(.7); }
    draw(a, { [i]: 'found' }); f.say(`${v} is in place. That took ${a.length - 1 - i} shift(s): inserting near the front costs O(n), inserting at the end costs O(1).`);
  }, true);
  f.btn('Delete', async () => {
    if (!a.length) return f.say('The array is empty.');
    const i = clamp(num(idx), 0, a.length - 1), t = a.slice(), gone = a[i];
    a = a.slice(0, i).concat(a.slice(i + 1));
    draw(t, { [i]: 'active' }); f.say(`Delete index ${i} (value ${gone}). The gap must be closed by shifting later elements left.`); await f.wait();
    t[i] = null;
    for (let j = i; j < t.length - 1; j++) { t[j] = t[j + 1]; t[j + 1] = null; draw(t, { [j]: 'active' }); f.say(`Shift ${t[j]} from index ${j + 1} to index ${j}.`); await f.wait(.7); }
    draw(a); f.say(`Removed ${gone}. ${a.length - i} shift(s) were needed.`);
  });
  f.btn('Access', async () => {
    if (!a.length) return f.say('The array is empty.');
    const i = clamp(num(idx), 0, a.length - 1);
    draw(a, { [i]: 'found' }); f.say(`a[${i}] = ${a[i]}. No scanning: the address is base + ${i} × element size, so access is O(1).`);
  });
  f.btn('Search', async () => {
    const v = num(val), seen = {};
    for (let i = 0; i < a.length; i++) {
      draw(a, { ...seen, [i]: 'active' }); f.say(`Is a[${i}] = ${a[i]} equal to ${v}?`); await f.wait(.7);
      if (a[i] === v) { draw(a, { ...seen, [i]: 'found' }); return f.say(`Found ${v} at index ${i} after ${i + 1} comparison(s). Linear search is O(n).`); }
      seen[i] = 'visited';
    }
    draw(a, seen); f.say(`${v} is not in the array. Every element was checked: ${a.length} comparison(s).`);
  });
  f.speed(); draw(a); f.say('Pick a value and an index, then try Insert, Delete, Access or Search.');
};

/* ---------- Linked list ---------- */
V.linkedlist = root => {
  const f = frame(root); let a = [8, 3, 15]; const CAP = 7;
  const val = f.input('Value', '21', { type: 'number' });
  const draw = (arr, marks = {}) => {
    const row = h('div', { class: 'll' }, h('span', { class: 'll-tag', text: 'head' }));
    arr.forEach((v, i) => row.append(h('span', { class: 'arrow', text: '→' }), h('div', { class: 'node ' + (marks[i] || '') }, h('b', { text: String(v) }), h('i', { text: 'next' }))));
    row.append(h('span', { class: 'arrow', text: '→' }), h('span', { class: 'll-null', text: 'null' }));
    f.stage.replaceChildren(row, legend());
  };
  const full = () => a.length >= CAP && (draw(a), f.say('That is enough nodes for the diagram. Delete one first.'), true);
  f.btn('Add at head', async () => {
    if (full()) return; const v = num(val); a = [v].concat(a);
    draw(a, { 0: 'found' }); f.say(`New node ${v} points at the old head, then head points at ${v}. Two pointer writes, no traversal: O(1).`);
  }, true);
  f.btn('Add at tail', async () => {
    if (full()) return; const v = num(val), old = a.slice(), seen = {}; a = a.concat([v]);
    for (let i = 0; i < old.length; i++) { draw(old, { ...seen, [i]: 'active' }); f.say(`Walk to node ${old[i]}${i === old.length - 1 ? ': its next is null, so this is the tail.' : ' and follow its next pointer.'}`); await f.wait(.7); seen[i] = 'visited'; }
    draw(a, { ...seen, [a.length - 1]: 'found' }); f.say(`Linked ${v} after the old tail. Without a tail pointer we had to walk ${old.length} node(s): O(n). Keep a tail pointer and it becomes O(1).`);
  });
  f.btn('Delete value', async () => {
    const v = num(val), seen = {};
    for (let i = 0; i < a.length; i++) {
      draw(a, { ...seen, [i]: 'active' }); f.say(`Is node ${a[i]} the one to delete?`); await f.wait(.7);
      if (a[i] === v) {
        const prev = i ? `node ${a[i - 1]}` : 'head'; const t = a.slice(); a = a.filter((_, k) => k !== i);
        draw(t, { ...seen, [i]: 'active' }); f.say(`Yes. Re-point ${prev} to skip over ${v}.`); await f.wait();
        draw(a); return f.say(`${v} is unlinked. No elements were shifted, only one pointer changed.`);
      }
      seen[i] = 'visited';
    }
    draw(a, seen); f.say(`${v} is not in the list.`);
  });
  f.btn('Search', async () => {
    const v = num(val), seen = {};
    for (let i = 0; i < a.length; i++) {
      draw(a, { ...seen, [i]: 'active' }); f.say(`Visit node ${a[i]}.`); await f.wait(.7);
      if (a[i] === v) { draw(a, { ...seen, [i]: 'found' }); return f.say(`Found ${v} after following ${i} pointer(s). There is no index to jump to, so search is O(n).`); }
      seen[i] = 'visited';
    }
    draw(a, seen); f.say(`Reached null without finding ${v}.`);
  });
  f.speed(); draw(a); f.say('Each node stores a value and a pointer to the next node. Try adding at the head and at the tail and compare the work.');
};

/* ---------- Stack ---------- */
V.stack = root => {
  const f = frame(root); let a = [4, 9, 2]; const CAP = 6;
  const val = f.input('Value', '7', { type: 'number' });
  const draw = (arr, marks = {}) => {
    const ptr = {}; if (arr.length) ptr[arr.length - 1] = 'top →';
    f.stage.replaceChildren(arr.length ? cells(arr, { marks, ptr, index: false, vertical: true }) : h('div', { class: 'viz-side', text: '(empty stack)' }));
  };
  f.btn('Push', async () => {
    if (a.length >= CAP) { draw(a); return f.say('Stack overflow: this demo stack holds ' + CAP + ' items.'); }
    const v = num(val); a = a.concat([v]); draw(a, { [a.length - 1]: 'found' }); f.say(`Pushed ${v}. It sits on top, so it will be the first to leave.`);
  }, true);
  f.btn('Pop', async () => {
    if (!a.length) { draw(a); return f.say('Stack underflow: nothing to pop.'); }
    const t = a.slice(), v = a[a.length - 1]; a = a.slice(0, -1);
    draw(t, { [t.length - 1]: 'active' }); f.say(`Pop removes the top item, ${v}.`); await f.wait();
    draw(a); f.say(`${v} is gone. ${a.length ? a[a.length - 1] + ' is the new top.' : 'The stack is empty.'}`);
  });
  f.btn('Peek', async () => {
    if (!a.length) { draw(a); return f.say('The stack is empty.'); }
    draw(a, { [a.length - 1]: 'found' }); f.say(`Peek returns ${a[a.length - 1]} without removing it.`);
  });
  draw(a); f.say('Last in, first out. Push a few values, then pop them and watch the order reverse.');
};

/* ---------- Queue ---------- */
V.queue = root => {
  const f = frame(root); let a = [5, 11, 6]; const CAP = 8;
  const val = f.input('Value', '9', { type: 'number' });
  const draw = (arr, marks = {}) => {
    const ptr = {}; if (arr.length) { ptr[0] = 'front'; ptr[arr.length - 1] = arr.length > 1 ? 'rear' : 'front/rear'; }
    f.stage.replaceChildren(arr.length ? cells(arr, { marks, ptr, index: false }) : h('div', { class: 'viz-side', text: '(empty queue)' }));
  };
  f.btn('Enqueue', async () => {
    if (a.length >= CAP) { draw(a); return f.say('The queue is full in this demo.'); }
    const v = num(val); a = a.concat([v]); draw(a, { [a.length - 1]: 'found' }); f.say(`Enqueued ${v} at the rear. It waits behind ${a.length - 1} item(s).`);
  }, true);
  f.btn('Dequeue', async () => {
    if (!a.length) { draw(a); return f.say('Nothing to dequeue.'); }
    const t = a.slice(), v = a[0]; a = a.slice(1);
    draw(t, { 0: 'active' }); f.say(`Dequeue removes the front item, ${v}: the one that has waited longest.`); await f.wait();
    draw(a); f.say(`${v} has left. ${a.length ? a[0] + ' is now at the front.' : 'The queue is empty.'}`);
  });
  f.btn('Peek', async () => {
    if (!a.length) { draw(a); return f.say('The queue is empty.'); }
    draw(a, { 0: 'found' }); f.say(`Peek returns the front item, ${a[0]}, and leaves it in place.`);
  });
  draw(a); f.say('First in, first out. Items join at the rear and leave from the front.');
};

/* ---------- Hash table ---------- */
V.hashtable = root => {
  const f = frame(root); const N = 7; let b = Array.from({ length: N }, () => []);
  const hash = k => [...k].reduce((t, c) => t + c.charCodeAt(0), 0);
  const explain = k => `hash("${k}") = ${[...k].map(c => c.charCodeAt(0)).join(' + ')} = ${hash(k)}; ${hash(k)} % ${N} = ${hash(k) % N}`;
  [['cat', 3], ['dog', 5], ['act', 8], ['owl', 2]].forEach(([k, v]) => b[hash(k) % N].push([k, v]));
  const key = f.input('Key', 'tac', { class: 'wide', maxlength: 8 }), val = f.input('Value', '42', { type: 'number' });
  const draw = (bucket = -1, hit = null, cls = 'found') => {
    f.stage.replaceChildren(h('div', { class: 'buckets' }, b.map((items, i) => h('div', { class: 'bucket' + (i === bucket ? ' active' : '') },
      h('span', { class: 'bi', text: String(i) }), items.map(([k, v]) => h('span', { class: 'chip ' + (k === hit ? cls : ''), text: `${k}: ${v}` }))))));
  };
  const k = () => (key.value.trim() || 'key').slice(0, 8);
  f.btn('Put', async () => {
    const kk = k(), v = num(val), i = hash(kk) % N, at = b[i].findIndex(e => e[0] === kk);
    const before = b[i].length; if (at >= 0) b[i][at][1] = v; else b[i].push([kk, v]);
    draw(i, at >= 0 ? kk : null, 'active'); f.say(explain(kk) + `. Go straight to bucket ${i}.`); await f.wait(1.6);
    draw(i, kk); f.say(at >= 0 ? `"${kk}" already exists, so its value is replaced with ${v}.` : before ? `Bucket ${i} already holds ${before} entr${before > 1 ? 'ies' : 'y'}: a collision. "${kk}" is chained onto the same bucket.` : `Bucket ${i} was empty. Stored "${kk}": ${v}.`);
  }, true);
  f.btn('Get', async () => {
    const kk = k(), i = hash(kk) % N;
    draw(i); f.say(explain(kk) + `. Only bucket ${i} needs checking.`); await f.wait(1.6);
    for (const [ek, ev] of b[i]) {
      draw(i, ek, 'active'); f.say(`Compare with "${ek}".`); await f.wait(.7);
      if (ek === kk) { draw(i, ek); return f.say(`Found "${kk}" → ${ev}. One hash plus a short chain scan: O(1) on average.`); }
    }
    draw(i); f.say(`"${kk}" is not in bucket ${i}, so it is not in the table.`);
  });
  f.btn('Remove', async () => {
    const kk = k(), i = hash(kk) % N, at = b[i].findIndex(e => e[0] === kk);
    draw(i, kk, 'active'); f.say(explain(kk) + '.'); await f.wait(1.4);
    if (at < 0) { draw(i); return f.say(`"${kk}" was not found in bucket ${i}.`); }
    b[i].splice(at, 1); draw(i); f.say(`Removed "${kk}" from bucket ${i}.`);
  });
  f.speed(); draw(); f.say('"cat" and "act" use the same letters, so this simple hash sends both to one bucket. Try Put with key "tac".');
};

/* ---------- Binary tree traversals ---------- */
const N_ = (val, left = null, right = null) => ({ val, left, right });
V.traversal = root => {
  const f = frame(root);
  const tree = N_(8, N_(3, N_(1), N_(6, N_(4), N_(7))), N_(10, null, N_(14, N_(13))));
  const order = { in: [], pre: [], post: [], level: [] };
  (function walk(n) { if (!n) return; order.pre.push(n); walk(n.left); order.in.push(n); walk(n.right); order.post.push(n); })(tree);
  for (const q = [tree]; q.length;) { const n = q.shift(); order.level.push(n); n.left && q.push(n.left); n.right && q.push(n.right); }
  const out = h('div', { class: 'viz-side' });
  const draw = (done = [], cur = null) => {
    f.stage.replaceChildren(treeSvg(tree, { kids: n => [n.left, n.right], label: n => n.val, cls: n => n === cur ? 'active' : done.includes(n) ? 'visited' : '' }), out);
    out.textContent = 'Output: ' + (done.concat(cur ? [cur] : []).map(n => n.val).join(' → ') || '…');
  };
  const info = {
    in: ['In-order', 'left subtree, node, right subtree. On a binary search tree this prints the values in sorted order.'],
    pre: ['Pre-order', 'node, left subtree, right subtree. The root comes first, which is why it is used to copy or serialise a tree.'],
    post: ['Post-order', 'left subtree, right subtree, node. Children are finished before their parent, which is what deleting a tree needs.'],
    level: ['Level-order', 'one level at a time, left to right, using a queue. This is breadth-first search on a tree.'],
  };
  for (const kind of Object.keys(info)) f.btn(info[kind][0], async () => {
    const seq = order[kind], done = [];
    f.say(`${info[kind][0]}: ${info[kind][1]}`); draw(); await f.wait(1.5);
    for (const n of seq) { draw(done, n); await f.wait(.9); done.push(n); }
    draw(done); f.say(`${info[kind][0]} visited every node exactly once: O(n) time. ${info[kind][1]}`);
  }, kind === 'in');
  f.speed(); draw(); f.say('Choose a traversal and watch the order in which the same tree is visited.');
};

/* ---------- Binary search tree ---------- */
V.bst = root => {
  const f = frame(root); let tree = null; const LIMIT = 15;
  const kids = n => [n.left, n.right];
  const ins = (n, v) => { if (!n) return N_(v); if (v < n.val) n.left = ins(n.left, v); else if (v > n.val) n.right = ins(n.right, v); return n; };
  const size = n => n ? 1 + size(n.left) + size(n.right) : 0;
  const path = v => { const p = []; for (let n = tree; n; n = v < n.val ? n.left : n.right) { p.push(n); if (n.val === v) break; } return p; };
  [50, 30, 70, 20, 40, 60, 80].forEach(v => { tree = ins(tree, v); });
  const val = f.input('Value', '65', { type: 'number' });
  const draw = (cls = () => '') => f.stage.replaceChildren(tree ? treeSvg(tree, { kids, label: n => n.val, cls }) : h('div', { class: 'viz-side', text: '(empty tree)' }));
  const walk = async (p, v, hide) => {
    const seen = new Set();
    for (const n of p) {
      if (n === hide) break;
      draw(x => x === hide ? 'hidden' : x === n ? 'active' : seen.has(x) ? 'visited' : '');
      f.say(v === n.val ? `${v} equals ${n.val}.` : `${v} is ${v < n.val ? 'smaller' : 'larger'} than ${n.val}, so go ${v < n.val ? 'left' : 'right'}.`);
      await f.wait(); seen.add(n);
    }
    return seen;
  };
  f.btn('Insert', async () => {
    const v = num(val);
    if (path(v).some(n => n.val === v)) { draw(n => n.val === v ? 'found' : ''); return f.say(`${v} is already in the tree. This BST keeps keys unique.`); }
    if (size(tree) >= LIMIT) { draw(); return f.say('The diagram is full. Delete a node or press Reset.'); }
    tree = ins(tree, v); const p = path(v), fresh = p[p.length - 1];
    const seen = await walk(p, v, fresh);
    draw(n => n === fresh ? 'found' : seen.has(n) ? 'visited' : ''); f.say(`Reached an empty spot after ${p.length - 1} comparison(s). ${v} becomes a new leaf.`);
  }, true);
  f.btn('Search', async () => {
    const v = num(val), p = path(v), seen = await walk(p, v), last = p[p.length - 1];
    if (last && last.val === v) { draw(n => n === last ? 'found' : seen.has(n) ? 'visited' : ''); f.say(`Found ${v} in ${p.length} step(s). Each comparison discards a whole subtree.`); }
    else { draw(n => seen.has(n) ? 'visited' : ''); f.say(`Fell off the tree: ${v} is not present.`); }
  });
  f.btn('Delete', async () => {
    const v = num(val), p = path(v), last = p[p.length - 1];
    const seen = await walk(p, v);
    if (!last || last.val !== v) { draw(n => seen.has(n) ? 'visited' : ''); return f.say(`${v} is not in the tree, nothing to delete.`); }
    let msg;
    if (last.left && last.right) {
      let sdr = last.right; while (sdr.left) sdr = sdr.left;
      draw(n => n === last ? 'active' : n === sdr ? 'found' : ''); f.say(`${v} has two children. Find its in-order successor: the smallest value in the right subtree, ${sdr.val}.`); await f.wait(1.8);
      msg = `Copied ${sdr.val} into the node, then removed the old ${sdr.val} leaf. The ordering rule still holds.`;
    } else msg = last.left || last.right ? `${v} had one child, so that child takes its place.` : `${v} was a leaf, so it is simply removed.`;
    const del = (n, x) => {
      if (!n) return null;
      if (x < n.val) n.left = del(n.left, x); else if (x > n.val) n.right = del(n.right, x);
      else { if (!n.left) return n.right; if (!n.right) return n.left; let m = n.right; while (m.left) m = m.left; n.val = m.val; n.right = del(n.right, m.val); }
      return n;
    };
    tree = del(tree, v); draw(); f.say(msg);
  });
  f.btn('Sorted insert', async () => {
    tree = null; [10, 20, 30, 40, 50].forEach(v => { tree = ins(tree, v); });
    draw(); f.say('Inserting already-sorted values gives a tree that leans one way: effectively a linked list, with O(n) search. Balanced trees (AVL, red-black) rotate nodes to prevent this.');
  });
  f.btn('Reset', async () => { tree = null; [50, 30, 70, 20, 40, 60, 80].forEach(v => { tree = ins(tree, v); }); draw(); f.say('Back to a balanced tree of seven nodes.'); });
  f.speed(); draw(); f.say('Left subtree < node < right subtree, at every node. Insert, search or delete a value to follow the path.');
};

/* ---------- Heap ---------- */
V.heap = root => {
  const f = frame(root); let a = [3, 8, 5, 14, 9, 12]; const CAP = 15;
  const val = f.input('Value', '2', { type: 'number' });
  const draw = (arr, marks = {}) => {
    const nodes = arr.map((v, i) => ({ v, i })); const kids = n => [nodes[2 * n.i + 1] || null, nodes[2 * n.i + 2] || null];
    f.stage.replaceChildren(...(arr.length ? [treeSvg(nodes[0], { kids, label: n => n.v, cls: n => marks[n.i] || '' }), cells(arr, { marks })] : [h('div', { class: 'viz-side', text: '(empty heap)' })]));
  };
  const play = async frames => { for (const [arr, marks, text, w] of frames) { draw(arr, marks); f.say(text); await f.wait(w || 1); } };
  f.btn('Insert', async () => {
    if (a.length >= CAP) { draw(a); return f.say('The diagram is full. Extract a few values first.'); }
    const v = num(val), t = a.concat([v]), fr = []; let i = t.length - 1;
    fr.push([t.slice(), { [i]: 'active' }, `Add ${v} at the next free slot (index ${i}) so the tree stays complete.`]);
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (t[p] <= t[i]) { fr.push([t.slice(), { [i]: 'found', [p]: 'visited' }, `Parent ${t[p]} ≤ ${t[i]}: the heap property holds, stop.`]); break; }
      fr.push([t.slice(), { [i]: 'active', [p]: 'active' }, `${t[i]} is smaller than its parent ${t[p]} (index ${p}): swap them (sift up).`]);
      [t[i], t[p]] = [t[p], t[i]]; i = p;
    }
    a = t.slice(); fr.push([t, { [i]: 'found' }, `${v} settled at index ${i}. At most one swap per level: O(log n).`, .1]);
    await play(fr);
  }, true);
  f.btn('Extract min', async () => {
    if (!a.length) { draw(a); return f.say('The heap is empty.'); }
    const t = a.slice(), min = t[0], fr = [];
    fr.push([t.slice(), { 0: 'found' }, `The minimum is always at the root: ${min}.`, 1.3]);
    const last = t.pop();
    if (t.length) {
      t[0] = last; fr.push([t.slice(), { 0: 'active' }, `Move the last item, ${last}, to the root, then repair downward (sift down).`, 1.3]);
      let i = 0;
      for (;;) {
        const l = 2 * i + 1, r = l + 1; let m = i;
        if (l < t.length && t[l] < t[m]) m = l; if (r < t.length && t[r] < t[m]) m = r;
        if (m === i) break;
        fr.push([t.slice(), { [i]: 'active', [m]: 'active' }, `${t[i]} is larger than its smaller child ${t[m]}: swap.`]);
        [t[i], t[m]] = [t[m], t[i]]; i = m;
      }
      fr.push([t.slice(), { [i]: 'found' }, `Heap repaired. Removed ${min} in O(log n).`, .1]);
    } else fr.push([[], {}, `Removed ${min}. The heap is now empty.`, .1]);
    a = t.slice(); await play(fr);
  });
  f.btn('Peek', async () => { if (!a.length) return f.say('The heap is empty.'); draw(a, { 0: 'found' }); f.say(`The minimum is ${a[0]}, read in O(1) from index 0.`); });
  f.speed(); draw(a); f.say('A min-heap drawn two ways: as a tree and as the array that actually stores it. Children of index i live at 2i+1 and 2i+2.');
};

/* ---------- Graph BFS / DFS ---------- */
V.graph = root => {
  const f = frame(root);
  const P = { A: [60, 40], B: [180, 40], C: [300, 40], D: [60, 150], E: [180, 150], F: [300, 150], G: [240, 245] };
  const E = [['A', 'B'], ['A', 'D'], ['B', 'C'], ['B', 'E'], ['D', 'E'], ['C', 'F'], ['E', 'G'], ['F', 'G']];
  const adj = {}; Object.keys(P).forEach(k => { adj[k] = []; }); E.forEach(([u, v]) => { adj[u].push(v); adj[v].push(u); });
  const start = f.select('Start', Object.keys(P).map(k => [k, 'Node ' + k]));
  const side = h('div', { class: 'viz-side' });
  const draw = (visited = [], cur = null, edge = null, frontier = '') => {
    const svg = s('svg', { viewBox: '0 0 360 285', role: 'img', 'aria-label': 'Graph with seven nodes' }); svg.style.maxWidth = '420px';
    E.forEach(([u, v]) => svg.append(s('line', { x1: P[u][0], y1: P[u][1], x2: P[v][0], y2: P[v][1], class: edge && edge.includes(u) && edge.includes(v) ? 'active' : '' })));
    Object.entries(P).forEach(([k, [x, y]]) => { const g = s('g', { class: k === cur ? 'active' : visited.includes(k) ? 'visited' : '' }); g.append(s('circle', { cx: x, cy: y, r: 19 }), s('text', { x, y }, k)); svg.append(g); });
    side.textContent = frontier; f.stage.replaceChildren(svg, side);
  };
  f.btn('Run BFS', async () => {
    const st = start.value, seen = [st], q = [st], order = [];
    draw([], null, null, `Queue: [${q}]`); f.say(`BFS from ${st}: put ${st} in a queue and mark it seen.`); await f.wait(1.3);
    while (q.length) {
      const u = q.shift(); order.push(u);
      draw(order, u, null, `Queue: [${q}]   Visited: ${order.join(' → ')}`); f.say(`Take ${u} from the front of the queue and look at its neighbours.`); await f.wait();
      for (const v of adj[u]) if (!seen.includes(v)) {
        seen.push(v); q.push(v);
        draw(order, u, [u, v], `Queue: [${q}]   Visited: ${order.join(' → ')}`); f.say(`${v} is new: mark it and add it to the back of the queue.`); await f.wait(.8);
      }
    }
    draw(order, null, null, `Visited: ${order.join(' → ')}`); f.say('BFS finished. Nodes were reached in order of distance from the start, which is why BFS finds shortest paths in unweighted graphs.');
  }, true);
  f.btn('Run DFS', async () => {
    const st = start.value, order = [], stack = [];
    const go = async (u, from) => {
      order.push(u); stack.push(u);
      draw(order, u, from ? [from, u] : null, `Call stack: [${stack}]   Visited: ${order.join(' → ')}`); f.say(`Visit ${u} and go deeper before trying anything else.`); await f.wait();
      for (const v of adj[u]) if (!order.includes(v)) await go(v, u);
      stack.pop();
      draw(order, stack[stack.length - 1] || null, null, `Call stack: [${stack}]   Visited: ${order.join(' → ')}`); f.say(`${u} has no unvisited neighbours left: backtrack.`); await f.wait(.7);
    };
    f.say(`DFS from ${st}: follow one path as far as it goes, then back up.`); draw(); await f.wait(1.3);
    await go(st, null);
    draw(order, null, null, `Visited: ${order.join(' → ')}`); f.say('DFS finished. It uses a stack (here, the call stack) instead of a queue.');
  });
  f.speed(); draw(); f.say('Pick a start node, then compare the order in which BFS and DFS visit the same graph.');
};

/* ---------- Trie ---------- */
V.trie = root => {
  const f = frame(root); const mk = ch => ({ ch, kids: {}, end: false }); const top = mk('•'); let count = 1;
  const add = w => { let n = top; const p = [top], fresh = new Set(); for (const c of w) { if (!n.kids[c]) { n.kids[c] = mk(c); fresh.add(n.kids[c]); count++; } n = n.kids[c]; p.push(n); } n.end = true; return [p, fresh]; };
  ['car', 'cat', 'cart', 'do', 'dog'].forEach(add);
  const word = f.input('Word', 'card', { class: 'wide', maxlength: 6 });
  const w = () => (word.value.toLowerCase().replace(/[^a-z]/g, '') || 'a').slice(0, 6);
  const draw = (cls = () => '') => f.stage.replaceChildren(treeSvg(top, { binary: false, kids: n => Object.keys(n.kids).sort().map(k => n.kids[k]), label: n => n.ch, cls: n => (cls(n) + (n.end ? ' end' : '')).trim() }),
    h('div', { class: 'viz-side', text: 'Thick ring = a complete word ends here' }));
  const follow = async (ww) => {
    let n = top; const seen = new Set([top]);
    for (let i = 0; i < ww.length; i++) {
      const c = ww[i], nx = n.kids[c];
      if (!nx) { draw(x => seen.has(x) ? 'visited' : ''); return [null, seen, `No "${c}" branch after "${ww.slice(0, i)}".`]; }
      draw(x => x === nx ? 'active' : seen.has(x) ? 'visited' : ''); f.say(`Follow the "${c}" branch.`); await f.wait(.8); seen.add(nx); n = nx;
    }
    return [n, seen, ''];
  };
  f.btn('Insert', async () => {
    const ww = w(); if (count + ww.length > 26) { draw(); return f.say('The diagram is full. Reload the page to start again.'); }
    const [p, fresh] = add(ww), shown = new Set([top]);
    for (let i = 1; i < p.length; i++) {
      shown.add(p[i]);
      draw(x => fresh.has(x) && !shown.has(x) ? 'hidden' : x === p[i] ? 'active' : shown.has(x) ? 'visited' : '');
      f.say(fresh.has(p[i]) ? `No "${ww[i - 1]}" branch yet: create a node.` : `"${ww[i - 1]}" already exists: reuse it (shared prefix).`); await f.wait(.8);
    }
    draw(x => x === p[p.length - 1] ? 'found' : shown.has(x) ? 'visited' : ''); f.say(`Marked the last node as the end of "${ww}". ${fresh.size} new node(s) were needed; the rest of the word was shared.`);
  }, true);
  f.btn('Search word', async () => {
    const ww = w(), [n, seen, why] = await follow(ww);
    if (!n) return f.say(`${why} "${ww}" is not stored.`);
    draw(x => x === n ? (n.end ? 'found' : 'active') : seen.has(x) ? 'visited' : '');
    f.say(n.end ? `"${ww}" is in the trie: ${ww.length} steps, however many words are stored.` : `The path exists, but no word ends here. "${ww}" is only a prefix.`);
  });
  f.btn('Starts with', async () => {
    const ww = w(), [n, seen, why] = await follow(ww);
    if (!n) return f.say(`${why} No stored word starts with "${ww}".`);
    const words = []; (function collect(x, acc) { if (x.end) words.push(acc); Object.keys(x.kids).sort().forEach(k => collect(x.kids[k], acc + k)); })(n, ww);
    const sub = new Set(); (function mark(x) { sub.add(x); Object.values(x.kids).forEach(mark); })(n);
    draw(x => sub.has(x) ? 'found' : seen.has(x) ? 'visited' : ''); f.say(`Everything below this node starts with "${ww}": ${words.join(', ')}. This is how autocomplete works.`);
  });
  f.speed(); draw(); f.say('Words that share a prefix share a path. Insert "card" and see how little is added.');
};

/* ---------- Binary search ---------- */
V.binarysearch = root => {
  const f = frame(root); let a;
  const fresh = () => { const set = new Set(); while (set.size < 13) set.add(rand(1, 99)); a = [...set].sort((x, y) => x - y); };
  fresh();
  const val = f.input('Target', String(a[9]), { type: 'number' });
  const draw = (lo, hi, mid, found) => {
    const marks = {}, ptr = {};
    a.forEach((_, i) => { if (lo != null && (i < lo || i > hi)) marks[i] = 'dim'; });
    if (mid != null) { marks[mid] = found ? 'found' : 'active'; }
    if (lo != null && lo <= hi) { ptr[lo] = 'lo'; ptr[hi] = ptr[hi] ? 'lo·hi' : 'hi'; }
    if (mid != null) ptr[mid] = ptr[mid] ? ptr[mid] + '·mid' : 'mid';
    f.stage.replaceChildren(cells(a, { marks, ptr }));
  };
  f.btn('Search', async () => {
    const t = num(val); let lo = 0, hi = a.length - 1, steps = 0;
    draw(lo, hi); f.say(`Look for ${t} in ${a.length} sorted values. Start with the whole range.`); await f.wait(1.3);
    while (lo <= hi) {
      const mid = lo + ((hi - lo) >> 1); steps++;
      draw(lo, hi, mid); f.say(`Step ${steps}: the middle is index ${mid}, value ${a[mid]}.`); await f.wait(1.2);
      if (a[mid] === t) { draw(lo, hi, mid, true); return f.say(`Found ${t} at index ${mid} in ${steps} step(s). A linear scan would have needed ${mid + 1}.`); }
      if (a[mid] < t) { lo = mid + 1; f.say(`${a[mid]} < ${t}: the target can only be to the right. Discard the left half.`); }
      else { hi = mid - 1; f.say(`${a[mid]} > ${t}: the target can only be to the left. Discard the right half.`); }
      draw(lo, hi); await f.wait(1.2);
    }
    draw(0, -1); f.say(`lo passed hi, so ${t} is not present. That took only ${steps} step(s) for ${a.length} values.`);
  }, true);
  f.btn('New array', async () => { fresh(); val.value = String(a[rand(0, 12)]); draw(); f.say('New sorted array. Binary search only works because the data is sorted.'); });
  f.speed(); draw(); f.say('Each step throws away half of what is left. Press Search.');
};

/* ---------- Sorting ---------- */
V.sorting = root => {
  const f = frame(root); let base = [], frames = [], at = 0, timer = null;
  const algo = f.select('Algorithm', [['bubble', 'Bubble sort'], ['selection', 'Selection sort'], ['insertion', 'Insertion sort'], ['merge', 'Merge sort'], ['quick', 'Quick sort']]);
  const size = f.select('Size', [['8', '8 values'], ['14', '14 values'], ['22', '22 values']]); size.value = '14';
  const build = (values, type) => {
    const a = values.slice(), out = []; let c = 0, w = 0; const n = a.length; const range = (lo, hi) => Array.from({ length: hi - lo }, (_, k) => lo + k);
    const push = (text, active = [], done = []) => out.push({ a: a.slice(), text, active, done, c, w });
    push('Unsorted input.');
    if (type === 'bubble') {
      for (let i = 0; i < n; i++) { let swapped = false; const done = range(n - i, n);
        for (let j = 0; j < n - i - 1; j++) { c++; if (a[j] > a[j + 1]) { [a[j], a[j + 1]] = [a[j + 1], a[j]]; w++; swapped = true; push(`${a[j + 1]} > ${a[j]}: swap so the larger value moves right.`, [j, j + 1], done); } else push(`${a[j]} ≤ ${a[j + 1]}: already in order.`, [j, j + 1], done); }
        if (!swapped) break; }
    } else if (type === 'selection') {
      for (let i = 0; i < n - 1; i++) { let m = i;
        for (let j = i + 1; j < n; j++) { c++; push(`Is ${a[j]} smaller than the current minimum ${a[m]}?`, [m, j], range(0, i)); if (a[j] < a[m]) m = j; }
        if (m !== i) { [a[i], a[m]] = [a[m], a[i]]; w++; } push(`Smallest remaining value ${a[i]} goes to position ${i}.`, [i], range(0, i + 1)); }
    } else if (type === 'insertion') {
      for (let i = 1; i < n; i++) { const key = a[i]; let j = i - 1; push(`Take ${key} and insert it into the sorted part on its left.`, [i], range(0, i));
        while (j >= 0) { c++; if (a[j] > key) { a[j + 1] = a[j]; a[j] = key; w++; push(`${a[j + 1]} > ${key}: shift it right.`, [j, j + 1], range(0, i)); j--; } else { push(`${a[j]} ≤ ${key}: ${key} stays here.`, [j, j + 1], range(0, i)); break; } } }
    } else if (type === 'merge') {
      const sort = (lo, hi) => { if (hi - lo <= 1) return; const mid = (lo + hi) >> 1; push(`Split positions ${lo}–${hi - 1} into two halves.`, range(lo, hi)); sort(lo, mid); sort(mid, hi);
        const L = a.slice(lo, mid), R = a.slice(mid, hi); let i = 0, j = 0, k = lo;
        while (i < L.length && j < R.length) { c++; a[k++] = L[i] <= R[j] ? L[i++] : R[j++]; w++; push(`Take the smaller front value, ${a[k - 1]}, from the two halves.`, [k - 1]); }
        while (i < L.length) { a[k++] = L[i++]; w++; } while (j < R.length) { a[k++] = R[j++]; w++; }
        push(`Positions ${lo}–${hi - 1} are merged in order.`, [], range(lo, hi)); };
      sort(0, n);
    } else {
      const fixed = []; const sort = (lo, hi) => { if (lo > hi) return; if (lo === hi) { fixed.push(lo); return; }
        const pivot = a[hi]; let i = lo; push(`Choose ${pivot} (last in range) as the pivot.`, [hi], fixed.slice());
        for (let j = lo; j < hi; j++) { c++; if (a[j] < pivot) { if (i !== j) { [a[i], a[j]] = [a[j], a[i]]; w++; } push(`${a[i]} < pivot ${pivot}: keep it on the left side.`, [i, hi], fixed.slice()); i++; } else push(`${a[j]} ≥ pivot ${pivot}: leave it on the right side.`, [j, hi], fixed.slice()); }
        [a[i], a[hi]] = [a[hi], a[i]]; w++; fixed.push(i); push(`Pivot ${pivot} lands in its final position, ${i}.`, [i], fixed.slice()); sort(lo, i - 1); sort(i + 1, hi); };
      sort(0, n - 1);
    }
    push('Sorted.', [], range(0, n)); return out;
  };
  const bars = h('div', { class: 'bars' }), stats = h('div', { class: 'stats' });
  const render = () => {
    const fr = frames[at], max = Math.max(...fr.a);
    bars.replaceChildren(...fr.a.map((v, i) => { const d = h('div', { class: fr.active.includes(i) ? 'active' : fr.done.includes(i) ? 'found' : '' }, fr.a.length <= 14 ? h('span', { text: String(v) }) : null); d.style.height = Math.max(6, v / max * 100) + '%'; return d; }));
    stats.replaceChildren(h('span', {}, 'Comparisons ', h('b', { text: String(fr.c) })), h('span', {}, 'Writes / swaps ', h('b', { text: String(fr.w) })), h('span', {}, 'Step ', h('b', { text: `${at} / ${frames.length - 1}` })));
    f.say(fr.text);
  };
  const stop = () => { clearTimeout(timer); timer = null; playBtn.textContent = 'Play'; };
  const reset = fresh => { stop(); if (fresh) base = Array.from({ length: +size.value }, () => rand(8, 99)); frames = build(base, algo.value); at = 0; render(); };
  const playBtn = h('button', { type: 'button', class: 'btn primary', text: 'Play', onclick: () => {
    if (timer) return stop(); if (at >= frames.length - 1) at = 0; playBtn.textContent = 'Pause';
    const tick = () => { if (at >= frames.length - 1) return stop(); at++; render(); timer = setTimeout(tick, f.delay() * .45); }; timer = setTimeout(tick, 0);
  } });
  f.controls.append(playBtn,
    h('button', { type: 'button', class: 'btn', text: 'Step', onclick: () => { stop(); if (at < frames.length - 1) { at++; render(); } } }),
    h('button', { type: 'button', class: 'btn', text: 'Back', onclick: () => { stop(); if (at > 0) { at--; render(); } } }),
    h('button', { type: 'button', class: 'btn', text: 'Shuffle', onclick: () => reset(true) }));
  f.speed(); algo.addEventListener('change', () => reset(false)); size.addEventListener('change', () => reset(true));
  f.stage.append(bars, stats); f.stage.style.paddingTop = '2.2rem'; reset(true);
};

/* ---------- Big-O growth ---------- */
V.bigo = root => {
  const f = frame(root);
  const rows = [['O(1)', () => 1], ['O(log n)', n => Math.max(1, Math.log2(n))], ['O(n)', n => n], ['O(n log n)', n => Math.max(1, n * Math.log2(n))], ['O(n²)', n => n * n], ['O(2ⁿ)', n => 2 ** n]];
  const range = h('input', { type: 'range', min: 1, max: 64, value: 16, 'aria-label': 'Input size n' }); range.style.width = '12rem';
  const out = h('b', { text: '16' });
  f.controls.append(h('label', { class: 'field' }, h('span', {}, 'Input size n = ', out), range));
  const fmt = v => v < 1e6 ? Math.round(v).toLocaleString('en') : v.toExponential(1).replace('e+', ' × 10^');
  const draw = () => {
    const n = +range.value; out.textContent = n; const top = Math.log10(2 ** 64);
    f.stage.replaceChildren(h('div', { class: 'growth' }, rows.map(([name, fn]) => { const v = fn(n); const bar = h('i'); bar.style.width = Math.max(0.5, Math.log10(v + 1) / top * 100) + '%'; return h('div', {}, h('code', { text: name }), bar, h('span', { text: fmt(v) + ' ops' })); })));
    f.say(`With n = ${n}: a linear algorithm does about ${n} steps, a quadratic one ${(n * n).toLocaleString('en')}, and an exponential one ${fmt(2 ** n)}. Bars use a logarithmic scale, otherwise only the last one would be visible.`);
  };
  range.addEventListener('input', draw); draw();
};

const boot = () => document.querySelectorAll('[data-viz]').forEach(el => { const fn = V[el.dataset.viz]; if (fn) fn(el); });
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();

/* Code tabs + copy. Remembers the reader's language across pages. */
(() => {
  const KEY = 'pl-lang';
  let saved = null; try { saved = localStorage.getItem(KEY); } catch (e) {}
  const select = (box, lang) => {
    box.querySelectorAll('[role=tab]').forEach(t => {
      const on = t.dataset.lang === lang; t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
    });
    box.querySelectorAll('pre').forEach(p => { p.hidden = p.dataset.lang !== lang; });
  };
  const init = () => document.querySelectorAll('.code').forEach(box => {
    const tabs = [...box.querySelectorAll('[role=tab]')];
    if (saved && tabs.some(t => t.dataset.lang === saved)) select(box, saved);
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => {
        document.querySelectorAll('.code').forEach(b => select(b, t.dataset.lang));
        try { localStorage.setItem(KEY, t.dataset.lang); } catch (e) {}
      });
      t.addEventListener('keydown', e => {
        const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { const n = tabs[(i + d + tabs.length) % tabs.length]; n.click(); n.focus(); }
      });
    });
    const copy = box.querySelector('.copy');
    if (copy) copy.addEventListener('click', async () => {
      const pre = box.querySelector('pre:not([hidden])');
      try { await navigator.clipboard.writeText(pre.textContent); copy.textContent = 'Copied'; }
      catch (e) { copy.textContent = 'Press Ctrl+C'; const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }
      setTimeout(() => { copy.textContent = 'Copy'; }, 1600);
    });
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

/* Hub search filter */
(() => {
  const init = () => {
    const box = document.getElementById('filter'); if (!box) return;
    const cards = [...document.querySelectorAll('[data-search]')], empty = document.getElementById('empty');
    box.addEventListener('input', () => {
      const q = box.value.trim().toLowerCase(); let shown = 0;
      cards.forEach(c => { const hit = !q || c.dataset.search.includes(q); c.hidden = !hit; if (hit) shown++; });
      document.querySelectorAll('[data-group]').forEach(g => { g.hidden = !g.querySelector('[data-search]:not([hidden])'); });
      empty.hidden = shown > 0;
    });
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
