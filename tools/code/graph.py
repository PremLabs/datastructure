from collections import deque


class Graph:
    """Undirected graph stored as an adjacency list."""

    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start):                 # O(V + E), uses a queue
        order, seen, queue = [], {start}, deque([start])
        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in self.adj[node]:
                if nxt not in seen:       # mark when queued, not when popped
                    seen.add(nxt)
                    queue.append(nxt)
        return order

    def dfs(self, start):                 # O(V + E), uses recursion
        order, seen = [], set()
        def visit(node):
            seen.add(node)
            order.append(node)
            for nxt in self.adj[node]:
                if nxt not in seen:
                    visit(nxt)
        visit(start)
        return order

    def shortest_path(self, start, goal):   # fewest edges, via BFS
        parent, queue = {start: None}, deque([start])
        while queue:
            node = queue.popleft()
            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]
            for nxt in self.adj[node]:
                if nxt not in parent:
                    parent[nxt] = node
                    queue.append(nxt)
        return None


g = Graph()
for u, v in ["AB", "AD", "BC", "BE", "DE", "CF", "EG", "FG"]:
    g.add_edge(u, v)
print(g.bfs("A"))                 # ['A', 'B', 'D', 'C', 'E', 'F', 'G']
print(g.dfs("A"))                 # ['A', 'B', 'C', 'F', 'G', 'E', 'D']
print(g.shortest_path("A", "G"))  # ['A', 'B', 'E', 'G']
