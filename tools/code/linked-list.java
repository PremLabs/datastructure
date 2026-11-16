public class LinkedList {
    private static class Node {
        int value;
        Node next;
        Node(int value, Node next) { this.value = value; this.next = next; }
    }

    private Node head;

    public void addFirst(int value) {              // O(1)
        head = new Node(value, head);
    }

    public void addLast(int value) {               // O(n) without a tail pointer
        Node node = new Node(value, null);
        if (head == null) { head = node; return; }
        Node current = head;
        while (current.next != null) current = current.next;
        current.next = node;
    }

    public boolean remove(int value) {             // O(n) to find, O(1) to unlink
        Node dummy = new Node(0, head);            // removes the head special case
        Node prev = dummy;
        while (prev.next != null && prev.next.value != value) prev = prev.next;
        if (prev.next == null) return false;
        prev.next = prev.next.next;
        head = dummy.next;
        return true;
    }

    public void reverse() {                        // O(n) time, O(1) space
        Node prev = null, current = head;
        while (current != null) {
            Node next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    @Override public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Node n = head; n != null; n = n.next) sb.append(n.value).append(n.next != null ? " -> " : "");
        return sb.toString();
    }

    public static void main(String[] args) {
        LinkedList items = new LinkedList();
        items.addLast(3); items.addLast(15);
        items.addFirst(8);                         // 8 -> 3 -> 15
        items.remove(3);                           // 8 -> 15
        items.reverse();                           // 15 -> 8
        System.out.println(items);
    }
}
