import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class BinaryTree {
    static class TreeNode {
        int value; TreeNode left, right;
        TreeNode(int value, TreeNode left, TreeNode right) { this.value = value; this.left = left; this.right = right; }
        TreeNode(int value) { this(value, null, null); }
    }

    static void inorder(TreeNode node, List<Integer> out) {      // left, node, right
        if (node == null) return;
        inorder(node.left, out);
        out.add(node.value);
        inorder(node.right, out);
    }

    static void preorder(TreeNode node, List<Integer> out) {     // node, left, right
        if (node == null) return;
        out.add(node.value);
        preorder(node.left, out);
        preorder(node.right, out);
    }

    static void postorder(TreeNode node, List<Integer> out) {    // left, right, node
        if (node == null) return;
        postorder(node.left, out);
        postorder(node.right, out);
        out.add(node.value);
    }

    static List<Integer> levelOrder(TreeNode root) {             // breadth-first, uses a queue
        List<Integer> out = new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();
        if (root != null) queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            out.add(node.value);
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        return out;
    }

    static int height(TreeNode node) {                           // edges on the longest path down
        return node == null ? -1 : 1 + Math.max(height(node.left), height(node.right));
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(8,
            new TreeNode(3, new TreeNode(1), new TreeNode(6, new TreeNode(4), new TreeNode(7))),
            new TreeNode(10, null, new TreeNode(14, new TreeNode(13), null)));

        List<Integer> out = new ArrayList<>();
        inorder(root, out);
        System.out.println(out);                  // [1, 3, 4, 6, 7, 8, 10, 13, 14]
        System.out.println(levelOrder(root));     // [8, 3, 10, 1, 6, 14, 4, 7, 13]
        System.out.println(height(root));         // 3
    }
}
