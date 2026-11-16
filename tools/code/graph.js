class Graph {
  adj = new Map();                         // adjacency list

  addEdge(u, v) {                          // undirected
    if (!this.adj.has(u)) this.adj.set(u, []);
    if (!this.adj.has(v)) this.adj.set(v, []);
    this.adj.get(u).push(v);
    this.adj.get(v).push(u);
  }

  bfs(start) {                             // O(V + E), uses a queue
    const order = [], seen = new Set([start]), queue = [start];
    for (let head = 0; head < queue.length; head++) {
      const node = queue[head];
      order.push(node);
      for (const next of this.adj.get(node)) {
        if (!seen.has(next)) { seen.add(next); queue.push(next); }  // mark when queued
      }
    }
    return order;
  }

  dfs(start) {                             // O(V + E), uses recursion
    const order = [], seen = new Set();
    const visit = node => {
      seen.add(node);
      order.push(node);
      for (const next of this.adj.get(node)) if (!seen.has(next)) visit(next);
    };
    visit(start);
    return order;
  }

  shortestPath(start, goal) {              // fewest edges, via BFS
    const parent = new Map([[start, null]]), queue = [start];
    for (let head = 0; head < queue.length; head++) {
      const node = queue[head];
      if (node === goal) {
        const path = [];
        for (let n = goal; n !== null; n = parent.get(n)) path.unshift(n);
        return path;
      }
      for (const next of this.adj.get(node)) {
        if (!parent.has(next)) { parent.set(next, node); queue.push(next); }
      }
    }
    return null;
  }
}

const g = new Graph();
['AB', 'AD', 'BC', 'BE', 'DE', 'CF', 'EG', 'FG'].forEach(([u, v]) => g.addEdge(u, v));
console.log(g.bfs('A'));                   // A B D C E F G
console.log(g.dfs('A'));                   // A B C F G E D
console.log(g.shortestPath('A', 'G'));     // A B E G
