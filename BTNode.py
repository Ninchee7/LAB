class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.leaf = leaf
        self.child = []

    def get_parent(self, root):
        if root is None or root == self:
            return None

        for child in root.child:
            if child == self:
                return root

            parent = self.get_parent(child)
            if parent:
                return parent

        return None

    def get_key(self):
        return self.key

    def set_key(self, new_key):
        self.keys = new_key

    def print_attributes(self):
        print("Node: BTreeNode")
        print("Key:", self.key)
        print("Leaf node:", self.leaf)
        child_keys = [child.key for child in self.child]
        print("Children keys:", child_keys)
        print()
