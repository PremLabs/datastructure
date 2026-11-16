// JavaScript arrays already grow for you. This class shows what happens underneath.
class DynamicArray {
  #data = new Array(2);
  #size = 0;

  get length() { return this.#size; }

  get(index) {                             // O(1)
    if (index < 0 || index >= this.#size) throw new RangeError('index out of range');
    return this.#data[index];
  }

  append(value) {                          // O(1) amortised
    if (this.#size === this.#data.length) this.#resize(this.#data.length * 2);
    this.#data[this.#size++] = value;
  }

  insert(index, value) {                   // O(n): shifts the tail right
    if (index < 0 || index > this.#size) throw new RangeError('index out of range');
    if (this.#size === this.#data.length) this.#resize(this.#data.length * 2);
    for (let i = this.#size; i > index; i--) this.#data[i] = this.#data[i - 1];
    this.#data[index] = value;
    this.#size++;
  }

  removeAt(index) {                        // O(n): shifts the tail left
    const value = this.get(index);
    for (let i = index; i < this.#size - 1; i++) this.#data[i] = this.#data[i + 1];
    this.#size--;
    return value;
  }

  #resize(capacity) {                      // O(n) copy, but rare
    const next = new Array(capacity);
    for (let i = 0; i < this.#size; i++) next[i] = this.#data[i];
    this.#data = next;
  }
}

const arr = new DynamicArray();
[12, 45, 7].forEach(v => arr.append(v));
arr.insert(1, 30);                         // 12, 30, 45, 7
arr.removeAt(0);                           // 30, 45, 7
console.log(Array.from({ length: arr.length }, (_, i) => arr.get(i)));
