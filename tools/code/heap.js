// JavaScript has no built-in heap, so this class is worth keeping around.
class MinHeap {
  #a = [];

  get size() { return this.#a.length; }
  peek() { return this.#a[0]; }                    // O(1)

  push(value) {                                    // O(log n)
    this.#a.push(value);
    this.#siftUp(this.#a.length - 1);
  }

  pop() {                                          // O(log n): remove the minimum
    if (this.#a.length === 0) throw new Error('pop from empty heap');
    const top = this.#a[0];
    const last = this.#a.pop();
    if (this.#a.length > 0) {
      this.#a[0] = last;
      this.#siftDown(0);
    }
    return top;
  }

  #siftUp(i) {
    const a = this.#a;
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (a[parent] <= a[i]) break;
      [a[parent], a[i]] = [a[i], a[parent]];
      i = parent;
    }
  }

  #siftDown(i) {
    const a = this.#a, n = a.length;
    for (;;) {
      let smallest = i;
      const left = 2 * i + 1, right = 2 * i + 2;
      if (left < n && a[left] < a[smallest]) smallest = left;
      if (right < n && a[right] < a[smallest]) smallest = right;
      if (smallest === i) return;
      [a[smallest], a[i]] = [a[i], a[smallest]];
      i = smallest;
    }
  }
}

const heap = new MinHeap();
[8, 3, 14, 5, 9].forEach(v => heap.push(v));
const out = [];
while (heap.size) out.push(heap.pop());
console.log(out);                                  // [3, 5, 8, 9, 14]
