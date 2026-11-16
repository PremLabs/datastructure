import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Trie {
    private static class Node {
        Map<Character, Node> children = new TreeMap<>();   // TreeMap keeps letters sorted
        boolean isWord;
    }

    private final Node root = new Node();

    public void insert(String word) {                      // O(L), L = word length
        Node node = root;
        for (char ch : word.toCharArray()) {
            node = node.children.computeIfAbsent(ch, k -> new Node());
        }
        node.isWord = true;
    }

    private Node find(String prefix) {
        Node node = root;
        for (char ch : prefix.toCharArray()) {
            node = node.children.get(ch);
            if (node == null) return null;
        }
        return node;
    }

    public boolean search(String word) {                   // O(L): whole word stored?
        Node node = find(word);
        return node != null && node.isWord;
    }

    public boolean startsWith(String prefix) {             // O(L)
        return find(prefix) != null;
    }

    public List<String> autocomplete(String prefix) {      // every stored word under the prefix
        List<String> results = new ArrayList<>();
        Node start = find(prefix);
        if (start != null) collect(start, new StringBuilder(prefix), results);
        return results;
    }

    private void collect(Node node, StringBuilder path, List<String> results) {
        if (node.isWord) results.add(path.toString());
        for (Map.Entry<Character, Node> e : node.children.entrySet()) {
            path.append(e.getKey());
            collect(e.getValue(), path, results);
            path.deleteCharAt(path.length() - 1);          // backtrack
        }
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        for (String word : new String[]{"car", "cat", "cart", "do", "dog"}) trie.insert(word);
        System.out.println(trie.search("car") + " " + trie.search("ca"));  // true false
        System.out.println(trie.startsWith("ca"));                         // true
        System.out.println(trie.autocomplete("ca"));                       // [car, cart, cat]
    }
}
