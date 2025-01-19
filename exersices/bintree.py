# -*- coding: utf-8 -*-
#bintree.py

class BinTree:

    def __init__(self, v, left=None, right=None):
        self.left = left
        self.right = right
        self.value = v

    def __repr__(self, prefix=""):
        result = str(self.value) + "\n"
        prefix += "=|"
        if self.left is not None:
            result += prefix + self.left.__repr__(prefix)
        if self.right is not None:
            result += prefix + self.right.__repr__(prefix)
        return result

    @classmethod
    def fromList(cls, lista):
        value, left, right = lista
        if left:
            left = cls.fromList(left)
        if right:
            right = cls.fromList(right)
        return cls(value, left, right)