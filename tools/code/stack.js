class Stack {
  #items = [];

  push(value) { this.#items.push(value); }        // O(1) amortised

  pop() {                                         // O(1)
    if (this.isEmpty()) throw new Error('pop from empty stack');
    return this.#items.pop();
  }

  peek() {                                        // O(1)
    if (this.isEmpty()) throw new Error('peek at empty stack');
    return this.#items[this.#items.length - 1];
  }

  isEmpty() { return this.#items.length === 0; }
}

// Classic stack problem: are the brackets in text balanced?
function isBalanced(text) {
  const pairs = { ')': '(', ']': '[', '}': '{' };
  const stack = new Stack();
  for (const ch of text) {
    if ('([{'.includes(ch)) stack.push(ch);
    else if (ch in pairs) {
      if (stack.isEmpty() || stack.pop() !== pairs[ch]) return false;
    }
  }
  return stack.isEmpty();
}

console.log(isBalanced('{[()]}'));                // true
console.log(isBalanced('([)]'));                  // false
