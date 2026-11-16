// Array.prototype.shift() is O(n), so a real queue keeps a moving head index instead.
class Queue {
  #items = [];
  #head = 0;

  enqueue(value) { this.#items.push(value); }     // O(1)

  dequeue() {                                     // O(1) amortised
    if (this.length === 0) throw new Error('dequeue from empty queue');
    const value = this.#items[this.#head++];
    if (this.#head > 32 && this.#head * 2 > this.#items.length) {
      this.#items = this.#items.slice(this.#head); // drop the used-up front
      this.#head = 0;
    }
    return value;
  }

  peek() { return this.#items[this.#head]; }
  get length() { return this.#items.length - this.#head; }
}

// Fixed-capacity queue on a plain array: the ring buffer.
class CircularQueue {
  #data; #head = 0; #size = 0;
  constructor(capacity) { this.#data = new Array(capacity); }

  enqueue(value) {
    if (this.#size === this.#data.length) throw new Error('queue is full');
    this.#data[(this.#head + this.#size) % this.#data.length] = value;
    this.#size++;
  }

  dequeue() {
    if (this.#size === 0) throw new Error('queue is empty');
    const value = this.#data[this.#head];
    this.#head = (this.#head + 1) % this.#data.length;
    this.#size--;
    return value;
  }
}

const q = new Queue();
['print', 'email', 'backup'].forEach(job => q.enqueue(job));
console.log(q.dequeue(), q.dequeue());            // print email

const ring = new CircularQueue(3);
ring.enqueue(1); ring.enqueue(2); ring.dequeue(); ring.enqueue(3); ring.enqueue(4);
console.log(ring.dequeue(), ring.dequeue(), ring.dequeue()); // 2 3 4
