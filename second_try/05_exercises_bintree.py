# 1. Write a recursive function that gets the root of a binary tree as a BinTree object, defined in
# the BinTree.py file. The function should return the number of nodes of the tree with an even value.

from bintree import BinTree

# def count_even_nodes(root):
#     if root is None:
#         return 0
#     count = (1 if root.value % 2== 0 else 0)
#     count += count_even_nodes(root.left)
#     count += count_even_nodes(root.right)
#     return count
#
# root = BinTree(1)
# root.left = BinTree(2, BinTree(4), BinTree(5))
# root.right = BinTree(3, None, BinTree(6))
#
#
# print(count_even_nodes(root))

# 2. Write a recursive function that gets the root of a binary tree as a BinTree object, defined in the BinTree.py file.
# The function should return the value obtained by adding the values of any node that is a left son and subtracting
# the values of any node that is a right son.

# def compute_tree_value(root, is_left=False):
#     if root is None:
#         return 0
#     left_sum = 0
#     right_sum = 0
#     if root.left:
#         left_sum += root.left.value + compute_tree_value(root.left)
#         right_sum += root.right.value + compute_tree_value(root.right)
#     return left_sum - right_sum
#
#
# root = BinTree(1)
# root.left = BinTree(2, BinTree(4), BinTree(5))
# root.right = BinTree(3, None, BinTree(6))
#
# print(compute_tree_value(root))


                           


















