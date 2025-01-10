#height of the tree
class BTNode1:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def height(self):
        '''returns the highest level in the tree'''
        height_left_subtree = 0
        height_right_subtree = 0

        if self.left_child:
            height_left_subtree = self.left_child.height()
        if self.right_child:
            height_right_subtree = self.right_child.height()

        return 1 + max(height_left_subtree, height_right_subtree)

# tree = BTNode1(0, BTNode1(1, BTNode1(3)), BTNode1(2,
#         BTNode1(4, BTNode1(5), BTNode1(6)), BTNode1(7, BTNode1(8), BTNode1(9))))
#
# print(tree.height())

#printing tree in ascii art
class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def __str__(self, level = 1):
        result = f'|--{self.value}' if level>1 else f'{self.value}'
        if self.left_child:
            result += '\n' + '   ' * (level-1) + self.left_child.__str__(level+1)
        if self.right_child:
            result += '\n' + '   ' * (level-1) + self.right_child.__str__(level+1)
        return result


# tree = BTNode(0, BTNode(1, BTNode(3)), BTNode(2,
#         BTNode(4, BTNode(5), BTNode(6)), BTNode(7, BTNode(8), BTNode(9))))
#
# print(tree)

class Node:
    def __init__(self, datum):
        self.datum = datum
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        child.parent = self
        self.children.remove(child)

class Tree:
    '''a simplt tree class'''
    def __init__(self, root=None):
        self.root = root


#create Nodes:
n1 = Node(0)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)

#Linking Nodes into the tree
t = Tree(n1)
n1.add_child(n2)
n1.add_child(n3)
n2.add_child(n4)
n2.add_child(n5)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.right = self.left = None
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def __find(self, node, parent, value):
#         if node is None:
#             return None, parent, False
#         if value == node.data:
#             return node, parent, True
#         if value < node.data:
#             if node.left:
#                 return self.__find(node.left, node, value)
#
#         if value > node.data:
#             if node.right:
#                 return self.__find(node.right, node, value)
#         return node, parent, False
#
#
#     def append(self, obj):
#         if self.root is None:
#             self.root = obj
#             return obj
#
#         s, p, fl_find = self.__find(self.root, None, obj.data)
#
#         if not fl_find and s:
#             if obj.data < s.data:
#                 s.left = obj
#             else:
#                 s.right = obj
#
#     def show_tree(self, node):
#         if node is None:
#             return
#
#         self.show_tree(node.left)
#         print(node.data)
#         self.show_tree(node.right)
#
#     def __del_leaf(self, s, p):
#         if p.left == s:
#             p.left = None
#         elif p.right == s:
#             p.right = None
#
# v = [10, 5, 7, 16, 13, 2, 20]
#
# t = Tree()
# for x in v:
#     t.append(Node(x))
#
# t.show_tree(t.root)