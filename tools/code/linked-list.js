class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  head = null;

  addFirst(value) {                        // O(1)
    this.head = new Node(value, this.head);
  }

  addLast(value) {                         // O(n) without a tail pointer
    const node = new Node(value);
    if (!this.head) { this.head = node; return; }
    let current = this.head;
    while (current.next) current = current.next;
    current.next = node;
  }

  remove(value) {                          // O(n) to find, O(1) to unlink
    const dummy = new Node(null, this.head); // removes the head special case
    let prev = dummy;
    while (prev.next && prev.next.value !== value) prev = prev.next;
    if (!prev.next) return false;
    prev.next = prev.next.next;
    this.head = dummy.next;
    return true;
  }

  reverse() {                              // O(n) time, O(1) space
    let prev = null, current = this.head;
    while (current) {
      [current.next, prev, current] = [prev, current, current.next];
    }
    this.head = prev;
  }

  *[Symbol.iterator]() {
    for (let n = this.head; n; n = n.next) yield n.value;
  }
}

const items = new LinkedList();
items.addLast(3); items.addLast(15);
items.addFirst(8);                         // 8 -> 3 -> 15
items.remove(3);                           // 8 -> 15
items.reverse();                           // 15 -> 8
console.log([...items]);
