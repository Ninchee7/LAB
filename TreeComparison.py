import matplotlib.pyplot as plt


class TreeComparison:
    @staticmethod
    def compare_insertions(b_tree, bst, keys):
        b_tree.insert_access_count = 0
        bst.insert_access_count = 0

        b_tree_accesses = []
        bst_accesses = []

        for key in keys:
            b_tree.insert(key)
            bst.insert(key)
            b_tree_accesses.append(b_tree.insert_access_count)
            bst_accesses.append(bst.insert_access_count)

        return b_tree_accesses, bst_accesses

        # print("Insertion Comparison:")
        # print("B-Tree disk accesses:", b_tree.insert_access_count)
        # print("Binary Search Tree disk accesses:", bst.insert_access_count)

        plt.plot(range(1, len(keys) + 1), b_tree_accesses, label='B_Tree')
        plt.plot(range(1, len(keys) + 1), bst_accesses, label='Binary Search Tree')
        plt.xlabel('Number of Insertion')
        plt.ylabel('Disk Accesses')
        plt.title('Comparison of Disk Accesses for Insertion')
        plt.legend()
        plt.show()

    @staticmethod
    def compare_searches(b_tree, bst, keys):
        b_tree.search_access_count = 0
        bst.search_access_count = 0

        b_tree_accesses = []
        bst_accesses = []

        for key in keys:
            b_tree.search(key)
            bst.search(key)
            b_tree_accesses.append(b_tree.search_access_count)
            bst_accesses.append(bst.search_access_count)

        return b_tree_accesses, bst_accesses

        # print("Search Comparison:")
        # print("B-Tree disk accesses:", b_tree.search_access_count)
        # print("Binary Search Tree disk accesses:", bst.search_access_count)



    @staticmethod
    def _count_disk_accesses(tree, keys, operation):
        count = 0
        for key in keys:
            if operation == "insert":
                tree.insert(key)
            elif operation == "search":
                tree.search(key)
            # Assuming each insertion or search operation reads or writes one node to disk
            count += 1
        return count
