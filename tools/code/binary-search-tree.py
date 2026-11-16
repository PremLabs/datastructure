class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):                # O(h), h = height
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node                       # equal keys are ignored

    def contains(self, key):              # O(h), iterative
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):                # O(h)
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:         # zero or one child
                return node.right
            if node.right is None:
                return node.left
            successor = node.right        # two children: smallest in right subtree
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def sorted_keys(self):                # in-order traversal
        out = []
        def walk(node):
            if node:
                walk(node.left); out.append(node.key); walk(node.right)
        walk(self.root)
        return out


tree = BST()
for key in (50, 30, 70, 20, 40, 60, 80):
    tree.insert(key)
tree.delete(50)                           # root with two children
print(tree.sorted_keys())                 # [20, 30, 40, 60, 70, 80]
print(tree.contains(60), tree.contains(50))   # True False
