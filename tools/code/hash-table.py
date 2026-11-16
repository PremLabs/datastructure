class HashTable:
    """Hash table with separate chaining and automatic resizing."""

    def __init__(self, capacity=8):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _index(self, key):
        return hash(key) % len(self._buckets)

    def put(self, key, value):            # O(1) average
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value           # key exists: overwrite
                return
        bucket.append([key, value])
        self._size += 1
        if self._size > 0.75 * len(self._buckets):   # load factor too high
            self._resize()

    def get(self, key, default=None):     # O(1) average
        for k, v in self._buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):                # O(1) average
        bucket = self._buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def _resize(self):                    # O(n): every key is rehashed
        old = self._buckets
        self._buckets = [[] for _ in range(len(old) * 2)]
        self._size = 0
        for bucket in old:
            for k, v in bucket:
                self.put(k, v)


table = HashTable()
for word in "the quick brown fox jumps over the lazy dog the end".split():
    table.put(word, table.get(word, 0) + 1)
print(table.get("the"), table.get("fox"), table.get("cat"))   # 3 1 None
