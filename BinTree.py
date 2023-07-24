from BinTNode import BinTreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.insert_access_count = 0
        self.search_access_count = 0

    def setRoot(self, key):
        self.root = BinTreeNode(key)

    def insert(self, key):
        self.insert_access_count += 1
        if self.root is None:
            self.setRoot(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        self.insert_access_count += 1
        if key < node.key:
            if node.left is None:
                node.left = BinTreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = BinTreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        self.search_access_count += 1
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        self.search_access_count += 1
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._get_successor(node.right)
                node.key = successor.key
                node.right = self._delete_recursive(node.right, successor.key)

        return node

    def _get_successor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def maximum(self):
        if self.root is None:
            return None
        return self._maximum_recursive(self.root)

    def _maximum_recursive(self, node):
        if node.right is None:
            return node
        return self._maximum_recursive(node.right)

    def minimum(self):
        if self.root is None:
            return None
        return self._minimum_recursive(self.root)

    def _minimum_recursive(self, node):
        if node.left is None:
            return node
        return self._minimum_recursive(node.left)

    def predecessor(self, key):
        node = self.search(key)
        if node is None:
            return None
        return self._predecessor_recursive(node)

    def _predecessor_recursive(self, node):
        if node.left is not None:
            return self._maximum_recursive(node.left)

        parent = node.get_parent(self.root)
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.get_parent(self.root)

        return parent

    def transplant(self, u, v):
        parent = u.get_parent(self.root)

        if parent is None:
            self.root = v
        elif u == parent.left:
            parent.left = v
        else:
            parent.right = v

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.key, end=" ")
            self._inorder_recursive(node.right)

    def print_tree(self):
        self._print_recursive(self.root)

    def _print_recursive(self, node):
        if node is not None:
            node.print_node()
            self._print_recursive(node.left)
            self._print_recursive(node.right)
