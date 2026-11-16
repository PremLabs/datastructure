class Node {
  constructor(key) { this.key = key; this.left = null; this.right = null; }
}

class BST {
  root = null;

  insert(key) { this.root = this.#insert(this.root, key); }   // O(h), h = height

  #insert(node, key) {
    if (!node) return new Node(key);
    if (key < node.key) node.left = this.#insert(node.left, key);
    else if (key > node.key) node.right = this.#insert(node.right, key);
    return node;                                              // equal keys are ignored
  }

  contains(key) {                                             // O(h), iterative
    let node = this.root;
    while (node) {
      if (key === node.key) return true;
      node = key < node.key ? node.left : node.right;
    }
    return false;
  }

  delete(key) { this.root = this.#delete(this.root, key); }   // O(h)

  #delete(node, key) {
    if (!node) return null;
    if (key < node.key) node.left = this.#delete(node.left, key);
    else if (key > node.key) node.right = this.#delete(node.right, key);
    else {
      if (!node.left) return node.right;                      // zero or one child
      if (!node.right) return node.left;
      let successor = node.right;                             // two children
      while (successor.left) successor = successor.left;
      node.key = successor.key;
      node.right = this.#delete(node.right, successor.key);
    }
    return node;
  }

  sortedKeys() {                                              // in-order traversal
    const out = [];
    const walk = node => { if (node) { walk(node.left); out.push(node.key); walk(node.right); } };
    walk(this.root);
    return out;
  }
}

const tree = new BST();
[50, 30, 70, 20, 40, 60, 80].forEach(key => tree.insert(key));
tree.delete(50);                                              // root with two children
console.log(tree.sortedKeys());                               // [20, 30, 40, 60, 70, 80]
console.log(tree.contains(60), tree.contains(50));            // true false
