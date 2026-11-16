import heapq


class MinHeap:
    def __init__(self):
        self._a = []

    def push(self, value):                # O(log n)
        self._a.append(value)
        self._sift_up(len(self._a) - 1)

    def pop(self):                        # O(log n): remove the minimum
        if not self._a:
            raise IndexError("pop from empty heap")
        top = self._a[0]
        last = self._a.pop()
        if self._a:
            self._a[0] = last
            self._sift_down(0)
        return top

    def peek(self):                       # O(1)
        return self._a[0]

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._a[parent] <= self._a[i]:
                break
            self._a[parent], self._a[i] = self._a[i], self._a[parent]
            i = parent

    def _sift_down(self, i):
        n = len(self._a)
        while True:
            smallest, left, right = i, 2 * i + 1, 2 * i + 2
            if left < n and self._a[left] < self._a[smallest]:
                smallest = left
            if right < n and self._a[right] < self._a[smallest]:
                smallest = right
            if smallest == i:
                return
            self._a[smallest], self._a[i] = self._a[i], self._a[smallest]
            i = smallest


heap = MinHeap()
for v in (8, 3, 14, 5, 9):
    heap.push(v)
print([heap.pop() for _ in range(5)])     # [3, 5, 8, 9, 14]

# In practice, use the standard library:
nums = [8, 3, 14, 5, 9]
heapq.heapify(nums)                       # O(n)
print(heapq.heappop(nums), heapq.nlargest(2, nums))   # 3 [14, 9]
