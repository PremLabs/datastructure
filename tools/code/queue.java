import java.util.ArrayDeque;
import java.util.Queue;

public class QueueDemo {
    /** Fixed-capacity queue on a plain array: the ring buffer. */
    static class CircularQueue {
        private final int[] data;
        private int head = 0, size = 0;

        CircularQueue(int capacity) { data = new int[capacity]; }

        void enqueue(int value) {                          // O(1)
            if (size == data.length) throw new IllegalStateException("queue is full");
            data[(head + size) % data.length] = value;
            size++;
        }

        int dequeue() {                                    // O(1)
            if (size == 0) throw new IllegalStateException("queue is empty");
            int value = data[head];
            head = (head + 1) % data.length;
            size--;
            return value;
        }
    }

    public static void main(String[] args) {
        Queue<String> q = new ArrayDeque<>();              // the standard FIFO queue
        q.offer("print"); q.offer("email"); q.offer("backup");
        System.out.println(q.poll() + " " + q.poll());     // print email

        CircularQueue ring = new CircularQueue(3);
        ring.enqueue(1); ring.enqueue(2); ring.dequeue(); ring.enqueue(3); ring.enqueue(4);
        System.out.println(ring.dequeue() + " " + ring.dequeue() + " " + ring.dequeue()); // 2 3 4
    }
}
