from collections import deque


class Queue:
    """FIFO queue. deque gives O(1) at both ends; list.pop(0) would be O(n)."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, value):             # O(1)
        self._items.append(value)

    def dequeue(self):                    # O(1)
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):                       # O(1)
        return self._items[0]

    def __len__(self):
        return len(self._items)


class CircularQueue:
    """Fixed-capacity queue on a plain array: the ring buffer."""

    def __init__(self, capacity):
        self._data = [None] * capacity
        self._head = 0
        self._size = 0

    def enqueue(self, value):
        if self._size == len(self._data):
            raise OverflowError("queue is full")
        tail = (self._head + self._size) % len(self._data)
        self._data[tail] = value
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError("queue is empty")
        value = self._data[self._head]
        self._head = (self._head + 1) % len(self._data)
        self._size -= 1
        return value


q = Queue()
for job in ("print", "email", "backup"):
    q.enqueue(job)
print(q.dequeue(), q.dequeue())           # print email

ring = CircularQueue(3)
ring.enqueue(1); ring.enqueue(2); ring.dequeue(); ring.enqueue(3); ring.enqueue(4)
print(ring.dequeue(), ring.dequeue(), ring.dequeue())   # 2 3 4
