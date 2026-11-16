from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(node, out):                   # left, node, right
    if node:
        inorder(node.left, out)
        out.append(node.value)
        inorder(node.right, out)
    return out

def preorder(node, out):                  # node, left, right
    if node:
        out.append(node.value)
        preorder(node.left, out)
        preorder(node.right, out)
    return out

def postorder(node, out):                 # left, right, node
    if node:
        postorder(node.left, out)
        postorder(node.right, out)
        out.append(node.value)
    return out

def level_order(root):                    # breadth-first, uses a queue
    out, queue = [], deque([root] if root else [])
    while queue:
        node = queue.popleft()
        out.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return out

def height(node):                         # edges on the longest path down
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


#         8
#       /   \
#      3     10
#     / \      \
#    1   6      14
#       / \    /
#      4   7  13
root = TreeNode(8,
                TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, None, TreeNode(14, TreeNode(13))))

print(inorder(root, []))      # [1, 3, 4, 6, 7, 8, 10, 13, 14]
print(preorder(root, []))     # [8, 3, 1, 6, 4, 7, 10, 14, 13]
print(postorder(root, []))    # [1, 4, 7, 6, 3, 13, 14, 10, 8]
print(level_order(root))      # [8, 3, 10, 1, 6, 14, 4, 7, 13]
print(height(root))           # 3
