class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

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

def sum_of_tree(root):
    if root.left is None and root.right is None:
        return root.value
    partial_sum = root.value
    if root.left:
        partial_sum += sum_of_tree(root.left)
    if root.right:
        partial_sum += sum_of_tree(root.right)
    return partial_sum

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.right), height(root.left))

root = BinaryNode(5)
node = BinaryNode(3)
root.left = node
node = BinaryNode(7)
root.right = node
node  = BinaryNode(1)
root.left.left = node
node = BinaryNode(4)
root.right.left = node
node = BinaryNode(9)
root.left.right = node
root.right.left.right = BinaryNode(8)

# print(count_nodes(root))
# print(count_leaves(root))
# print(sum_of_tree(root))
# print(height(root))

class TreeNode:
    def __init__(self, val, sons=None):
        self.value = val
        if sons:
            self.sons = sons
        else:
            self.sons = []

    def __repr__(self):
        return str(self.value)

sons = [TreeNode(3), TreeNode(5)]
root = TreeNode(7, sons)
node = TreeNode(3)
root = TreeNode(2, [node, root])
root = TreeNode(9, [root])
node = TreeNode(1, [TreeNode(9), TreeNode(7), TreeNode(3)])
root = TreeNode(5, [root, TreeNode(8), node])

# print(root.sons)
# print(root.sons[0].value)
# print(root.sons[1].value)
# print(root.sons[2].sons)
# print(root.sons[2].sons[0].value)

def count_tree_nodes(root):
    if len(root.sons)==0:
        return 1
    counter = 1
    for tree in root.sons:
        counter += count_tree_nodes(tree)
    return counter

# print(count_tree_nodes(root))








