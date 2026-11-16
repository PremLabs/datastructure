import java.util.ArrayList;
import java.util.List;

public class BST {
    private static class Node {
        int key; Node left, right;
        Node(int key) { this.key = key; }
    }

    private Node root;

    public void insert(int key) { root = insert(root, key); }       // O(h), h = height

    private Node insert(Node node, int key) {
        if (node == null) return new Node(key);
        if (key < node.key) node.left = insert(node.left, key);
        else if (key > node.key) node.right = insert(node.right, key);
        return node;                                                // equal keys are ignored
    }

    public boolean contains(int key) {                              // O(h), iterative
        Node node = root;
        while (node != null) {
            if (key == node.key) return true;
            node = key < node.key ? node.left : node.right;
        }
        return false;
    }

    public void delete(int key) { root = delete(root, key); }       // O(h)

    private Node delete(Node node, int key) {
        if (node == null) return null;
        if (key < node.key) node.left = delete(node.left, key);
        else if (key > node.key) node.right = delete(node.right, key);
        else {
            if (node.left == null) return node.right;               // zero or one child
            if (node.right == null) return node.left;
            Node successor = node.right;                            // two children
            while (successor.left != null) successor = successor.left;
            node.key = successor.key;
            node.right = delete(node.right, successor.key);
        }
        return node;
    }

    public List<Integer> sortedKeys() {                             // in-order traversal
        List<Integer> out = new ArrayList<>();
        walk(root, out);
        return out;
    }

    private void walk(Node node, List<Integer> out) {
        if (node == null) return;
        walk(node.left, out); out.add(node.key); walk(node.right, out);
    }

    public static void main(String[] args) {
        BST tree = new BST();
        for (int key : new int[]{50, 30, 70, 20, 40, 60, 80}) tree.insert(key);
        tree.delete(50);                                            // root with two children
        System.out.println(tree.sortedKeys());                      // [20, 30, 40, 60, 70, 80]
        System.out.println(tree.contains(60) + " " + tree.contains(50)); // true false
    }
}
