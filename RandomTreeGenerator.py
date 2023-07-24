import random
from copy import deepcopy
from BTree import BTree
from BinTree import BinarySearchTree


class RandomTreeGenerator:
    @staticmethod
    def generate_b_tree(size, t):
        if size <= 0:
            return None
        keys = random.sample(range(1, 1000), min(size, 1000))
        b_tree = BTree(t)
        for key in keys[:size]:
            b_tree.insert(key)
        return deepcopy(b_tree)

    @staticmethod
    def generate_binary_search_tree(size):
        if size <= 0:
            return None
        keys = random.sample(range(1, 1000), min(size, 1000))
        bst = BinarySearchTree()
        for key in keys[:size]:
            bst.insert(key)
        return deepcopy(bst)
