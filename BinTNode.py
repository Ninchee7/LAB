class BinTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_parent(self, root):
        if root is None or root == self:
            return None
        if (root.left == self) or (root.right == self):
            return root
        if self.key < root.key:
            return self.get_parent(root.left)
        else:
            return self.get_parent(root.right)

    def get_key(self):
        return self.key

    def set_key(self, new_key):
        self.key = new_key

    def get_name(self):
        return "Node"

    def get_childern(self):
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children

    def print_node(self):
        print("Node:", self.get_name())
        print("key:", self.key)
        if self.left is not None:
            print("Left Child:", self.left.key)
        if self.right is not None:
            print("Right Child:", self.right.key)
        print()
