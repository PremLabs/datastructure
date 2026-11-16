class TreeNode {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

function inorder(node, out = []) {         // left, node, right
  if (node) { inorder(node.left, out); out.push(node.value); inorder(node.right, out); }
  return out;
}

function preorder(node, out = []) {        // node, left, right
  if (node) { out.push(node.value); preorder(node.left, out); preorder(node.right, out); }
  return out;
}

function postorder(node, out = []) {       // left, right, node
  if (node) { postorder(node.left, out); postorder(node.right, out); out.push(node.value); }
  return out;
}

function levelOrder(root) {                // breadth-first, uses a queue
  const out = [], queue = root ? [root] : [];
  for (let head = 0; head < queue.length; head++) {
    const node = queue[head];
    out.push(node.value);
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
  return out;
}

const height = node =>                     // edges on the longest path down
  node ? 1 + Math.max(height(node.left), height(node.right)) : -1;

const T = (v, l, r) => new TreeNode(v, l, r);
const root = T(8, T(3, T(1), T(6, T(4), T(7))), T(10, null, T(14, T(13))));

console.log(inorder(root));                // [1, 3, 4, 6, 7, 8, 10, 13, 14]
console.log(preorder(root));               // [8, 3, 1, 6, 4, 7, 10, 14, 13]
console.log(postorder(root));              // [1, 4, 7, 6, 3, 13, 14, 10, 8]
console.log(levelOrder(root));             // [8, 3, 10, 1, 6, 14, 4, 7, 13]
console.log(height(root));                 // 3
