# This is a sample Python script.
import random

from matplotlib import pyplot as plt

from RandomTreeGenerator import RandomTreeGenerator
from BinTree import BinarySearchTree
from BTree import BTree
from TreeComparison import TreeComparison

#  Numero di esecuzioni del programma
num_iterations = 5
size = 10
t = 3

#  Liste per raccogliere i risultati di ciascuna iterazione
insertion_results_b_tree = []
insertion_results_bst = []
search_results_b_tree = []
search_results_bst = []

for _ in range(num_iterations):
    #  Generazione nuove chiavi casuali per ogni interazione
    keys = random.sample(range(1, 1000), size)
    # Generazione alberi casuali
    bst = RandomTreeGenerator.generate_binary_search_tree(size)  # Creazione di un albero binario di ricerca
    b_tree = RandomTreeGenerator.generate_b_tree(size, t)  # Creazione di un B albero

    # Confronto e raccolta risultati
    b_tree_accesses, bst_accesses = TreeComparison.compare_insertions(b_tree, bst, keys)
    insertion_results_bst.append(sum(bst_accesses))
    insertion_results_b_tree.append(sum(b_tree_accesses))

    b_tree_accesses, bst_accesses = TreeComparison.compare_searches(b_tree, bst, keys)
    search_results_bst.append(sum(bst_accesses))
    search_results_b_tree.append(sum(b_tree_accesses))

# Calcolo della media dei risultati
average_insertion_b_tree = sum(insertion_results_b_tree) / num_iterations
average_insertion_bst = sum(insertion_results_bst) / num_iterations
average_search_b_tree = sum(search_results_b_tree) / num_iterations
average_search_bst = sum(search_results_bst) / num_iterations

# Stampa risultati medi
print("AVG Disk Accesses for Insertion in B-Tree:", average_insertion_b_tree)
print("AVG Disk Accesses for Insertion in Binary Search Tree:", average_insertion_bst)
print("AVG Disk Accesses for Search in B-Tree:", average_search_b_tree)
print("AVG Disk Accesses for Search in Binary Search Tree:", average_search_bst)

plt.plot(range(1, num_iterations + 1), insertion_results_b_tree, label='B_Tree')
plt.plot(range(1, num_iterations + 1), insertion_results_bst, label='Binary Search Tree')
plt.xlabel('Iteration')
plt.ylabel('Total Disk Accesses')
plt.title('Comparison of Disk Accesses for Insertion')
plt.legend()
plt.show()

plt.plot(range(1, num_iterations + 1), search_results_b_tree, label='B_Tree')
plt.plot(range(1, num_iterations + 1), search_results_bst, label='Binary Search Tree')
plt.xlabel('Iteration')
plt.ylabel('Total Disk Accesses')
plt.title('Comparison of Disk Accesses for Search')
plt.legend()
plt.show()
