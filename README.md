# Data Structures and Algorithms in Python

## Purpose

This repository serves as my personal knowledge base and collection of Python implementations for common Data Structures and Algorithms (DS&A). It represents a consolidation of concepts I've studied and refined over time. The focus is on clear, understandable code that translates theoretical knowledge into working implementations.

## What's Included

This collection currently includes implementations for:

* **1. Hash Tables:**
    * `1a HashTable_NoCollisionHandling.py`: A basic hash table implementation that **does not handle hash collisions**. This version is for illustrative purposes of basic hashing.
    * `1b HashTable_SeparateChaining.py`: Hash table using separate chaining for collision resolution.
    * `1c HashTable_LinearProbing.py`: Hash table using linear probing for collision resolution.
* **2. Linked Lists:**
    * `2a LinkedList.py`: Singly linked list.
    * `2b DoublyLinkedList.py`: Doubly linked list.
* **3. Stacks & Queues:**
    * `3 Stack.py`: Stack implementation (includes discussion/examples using both Python lists and `collections.deque`).
    * `4 Queue.py`: Queue implementation (includes discussion/examples using both Python lists and `collections.deque`).
* **5. Trees, Heaps & Tries:**
    * `5a Tree.py`: A general-purpose tree (N-ary tree).
    * `5b BinarySearchTree.py`: Binary Search Tree (BST) with common operations including iterative traversals.
    * `5c MinHeap.py`: Min-Heap implementation using an array.
    * `5d MaxHeap.py`: Max-Heap implementation using an array.
    * `5e Trie.py`: Trie (prefix tree) implementation.
* **6. Graphs:**
    * `6a Graph.py`: Graph representations (Adjacency List and Adjacency Matrix) with various algorithms like BFS/DFS for pathfinding, connectivity checks, and topological sort (Kahn's algorithm).
    * `6b Dijkstra.py`: Dijkstra's algorithm for shortest paths (versions for Adjacency List and Adjacency Matrix).
* **7. Searching Algorithms:**
    * `7 BinarySearch.py`: Binary Search (iterative and recursive versions), and Linear Search.
* **8. Sorting Algorithms (Basic):**
    * `8 SelectionSort.py`: Selection Sort.
    * `9 BubbleSort.py`: Bubble Sort (with optimization).
* **10. Sorting Algorithms (Intermediate):**
    * `10a InsertionSort.py`: Insertion Sort.
    * `10b ShellSort.py`: Shell Sort.
* **11. Sorting Algorithms (Divide & Conquer):**
    * `11 MergeSort.py`: Merge Sort (in-place modification version).
    * `12 QuickSort.py`: Quick Sort (using Hoare partition scheme).
* **13. Disjoint Set Union (DSU):**
    * `13 UnionFind.py`: Union-Find data structure with path compression and union by rank optimizations.
* **14. Minimum Spanning Tree (MST) Algorithms:**
    * `14 Kruskal_And_Prim.py`: Implementations of Kruskal's algorithm (typically for sparse graphs) and Prim's algorithm (adjacency matrix version, suitable for dense graphs).

*(Note: The file naming convention `1a, 1b, ...` is used to group related concepts or show a progression of implementations, though some names have been made more descriptive.)*

## My Approach

The implementations in this collection reflect an ongoing effort to:
* Solidify understanding of the core logic and intricacies of each data structure and algorithm.
* Explore and document different implementation strategies and their trade-offs (e.g., various hash table collision resolution techniques, different backends for stacks/queues)
* Maintain clear, understandable, and well-commented Python code that serves as a reliable personal reference.

## Testing Status & Disclaimer

**Important:** While the core logic of these implementations has been developed and tested with basic examples (often found within `if __name__ == '__main__':` blocks in the respective files), this collection **does not currently include a comprehensive suite of formal unit tests.**

These implementations are intended for **educational, illustrative, and personal reference purposes only**. They should not be considered production-ready or used in critical applications without further rigorous testing and potential refinement.

## How to Use

Most files contain an `if __name__ == '__main__':` block with example usage. You can typically run these Python files directly to see a basic demonstration of the data structure or algorithm in action.