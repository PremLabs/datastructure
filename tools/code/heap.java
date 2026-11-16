import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class MinHeap {
    private final List<Integer> a = new ArrayList<>();

    public void push(int value) {                      // O(log n)
        a.add(value);
        siftUp(a.size() - 1);
    }

    public int pop() {                                 // O(log n): remove the minimum
        if (a.isEmpty()) throw new IllegalStateException("pop from empty heap");
        int top = a.get(0);
        int last = a.remove(a.size() - 1);
        if (!a.isEmpty()) {
            a.set(0, last);
            siftDown(0);
        }
        return top;
    }

    public int peek() { return a.get(0); }             // O(1)

    private void siftUp(int i) {
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (a.get(parent) <= a.get(i)) break;
            Collections.swap(a, parent, i);
            i = parent;
        }
    }

    private void siftDown(int i) {
        int n = a.size();
        while (true) {
            int smallest = i, left = 2 * i + 1, right = 2 * i + 2;
            if (left < n && a.get(left) < a.get(smallest)) smallest = left;
            if (right < n && a.get(right) < a.get(smallest)) smallest = right;
            if (smallest == i) return;
            Collections.swap(a, smallest, i);
            i = smallest;
        }
    }

    public static void main(String[] args) {
        MinHeap heap = new MinHeap();
        for (int v : new int[]{8, 3, 14, 5, 9}) heap.push(v);
        for (int i = 0; i < 5; i++) System.out.print(heap.pop() + " ");   // 3 5 8 9 14
        System.out.println();

        // In practice, use the standard library:
        PriorityQueue<Integer> pq = new PriorityQueue<>(List.of(8, 3, 14, 5, 9));
        System.out.println(pq.poll());                                    // 3
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(List.of(8, 3, 14));
        System.out.println(maxHeap.peek());                               // 14
    }
}
