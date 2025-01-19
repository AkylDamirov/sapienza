#1. Write a function to find the height of a binary tree.
#2. Calculate the total number of nodes in a binary tree.
#3. Count the number of leaf nodes in a binary tree.

class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return -1
    left_node = height(root.left)
    right_node = height(root.right)
    return 1 + max(left_node, right_node)

def count_nodes(root):
    if root.left is None and root.right is None:
        return 1
    counter = 1
    if root.left:
        counter += count_nodes(root.left)
    if root.right:
        counter += count_nodes(root.right)
    return counter

def count_leaves(root):
    if root.left is None and root.right is None:
        return 1
    counter = 0
    if root.left:
        counter += count_leaves(root.left)
    if root.right:
        counter += count_leaves(root.right)
    return counter


root = BinaryNode(1)
root.left = BinaryNode(2, BinaryNode(4), BinaryNode(5))
root.right = BinaryNode(3, None, BinaryNode(6))

# print(height(root))
# print(count_nodes(root))
print(count_leaves(root))





















