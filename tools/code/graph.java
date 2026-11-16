import java.util.*;

public class Graph {
    private final Map<String, List<String>> adj = new LinkedHashMap<>();

    public void addEdge(String u, String v) {              // undirected
        adj.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
        adj.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
    }

    public List<String> bfs(String start) {                // O(V + E), uses a queue
        List<String> order = new ArrayList<>();
        Set<String> seen = new HashSet<>(List.of(start));
        Queue<String> queue = new ArrayDeque<>(List.of(start));
        while (!queue.isEmpty()) {
            String node = queue.poll();
            order.add(node);
            for (String next : adj.get(node)) {
                if (seen.add(next)) queue.offer(next);     // mark when queued
            }
        }
        return order;
    }

    public List<String> dfs(String start) {                // O(V + E), uses recursion
        List<String> order = new ArrayList<>();
        visit(start, new HashSet<>(), order);
        return order;
    }

    private void visit(String node, Set<String> seen, List<String> order) {
        seen.add(node);
        order.add(node);
        for (String next : adj.get(node)) {
            if (!seen.contains(next)) visit(next, seen, order);
        }
    }

    public List<String> shortestPath(String start, String goal) {   // fewest edges, via BFS
        Map<String, String> parent = new HashMap<>();
        parent.put(start, null);
        Queue<String> queue = new ArrayDeque<>(List.of(start));
        while (!queue.isEmpty()) {
            String node = queue.poll();
            if (node.equals(goal)) {
                LinkedList<String> path = new LinkedList<>();
                for (String n = goal; n != null; n = parent.get(n)) path.addFirst(n);
                return path;
            }
            for (String next : adj.get(node)) {
                if (!parent.containsKey(next)) { parent.put(next, node); queue.offer(next); }
            }
        }
        return null;
    }

    public static void main(String[] args) {
        Graph g = new Graph();
        for (String e : new String[]{"AB", "AD", "BC", "BE", "DE", "CF", "EG", "FG"}) {
            g.addEdge(e.substring(0, 1), e.substring(1));
        }
        System.out.println(g.bfs("A"));                // [A, B, D, C, E, F, G]
        System.out.println(g.dfs("A"));                // [A, B, C, F, G, E, D]
        System.out.println(g.shortestPath("A", "G"));  // [A, B, E, G]
    }
}
