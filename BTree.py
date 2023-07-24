from BTNode import BTreeNode


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t
        self.insert_access_count = 0
        self.search_access_count = 0

    def insert(self, k):
        self.insert_access_count += 1
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, key):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
            self.insert_access_count += 1
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], key)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.append(z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: 2 * t]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def search(self, k, x=None):
        if x is None:
            x = self.root

        self.search_access_count += 1
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return x
            elif x.leaf:
                return None
            elif i < len(x.child):
                return self.search(k, x.child[i])

    def print_btree(self):
        self.print_btree_recursive(self.root, "")

    def print_btree_recursive(self, node, level):
        if node:
            print(level + "keys:", node.keys)
            if not node.leaf:
                for i, child in enumerate(node.child):
                    print(level + "child:", i + 1)
                    self.print_btree_recursive(child, level + "\t")
