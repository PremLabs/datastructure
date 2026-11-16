class DynamicArray:
    """A growable array built on a fixed-size block, like Python's list."""

    def __init__(self):
        self._capacity = 2
        self._size = 0
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def get(self, index):                 # O(1)
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        return self._data[index]

    def append(self, value):              # O(1) amortised
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):       # O(n): shifts the tail right
        if not 0 <= index <= self._size:
            raise IndexError("index out of range")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove_at(self, index):           # O(n): shifts the tail left
        value = self.get(index)
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        self._data[self._size] = None
        return value

    def _resize(self, capacity):          # O(n) copy, but rare
        new_data = [None] * capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data, self._capacity = new_data, capacity


arr = DynamicArray()
for v in (12, 45, 7):
    arr.append(v)
arr.insert(1, 30)                         # 12, 30, 45, 7
arr.remove_at(0)                          # 30, 45, 7
print([arr.get(i) for i in range(len(arr))])
