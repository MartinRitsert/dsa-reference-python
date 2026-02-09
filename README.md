# Data Structures and Algorithms in Python

## 🎯 Purpose

This repository serves as my personal knowledge base and collection of Python implementations for common Data Structures and Algorithms (DS&A). It represents a consolidation of concepts I've studied and refined over time. The focus is on clear, understandable code that translates theoretical knowledge into working implementations.

## 📚 What's Included

This collection currently includes implementations for:

* **1. Hash Tables** 🗂️
    * `01a_HashTable_NoCollisionHandling.py`: A basic hash table implementation that **does not handle hash collisions**. This version is for illustrative purposes of basic hashing.
    * `01b_HashTable_SeparateChaining.py`: Hash table using separate chaining for collision resolution.
    * `01c_HashTable_LinearProbing.py`: Hash table using linear probing for collision resolution.
* **2. Linked Lists** 🔗
    * `02a_LinkedList.py`: Singly linked list.
    * `02b_DoublyLinkedList.py`: Doubly linked list.
* **3. Stacks** 📚
    * `03_Stack.py`: Stack implementation (includes discussion/examples using both Python lists and `collections.deque`).
* **4. Queues** 🚶‍♀️🚶‍♂️🚶
    * `04_Queue.py`: Queue implementation (includes discussion/examples using both Python lists and `collections.deque`).
* **5. Trees, Heaps & Tries** 🌳
    * `05a_Tree.py`: A general-purpose tree (N-ary tree).
    * `05b_BinarySearchTree.py`: Binary Search Tree (BST) with common operations including iterative traversals.
    * `05c_MinHeap.py`: Min-Heap implementation using an array.
    * `05d_MaxHeap.py`: Max-Heap implementation using an array.
    * `05e_Trie.py`: Trie (prefix tree) implementation.
* **6. Graphs** 📍➖📍➖📍
    * `06a_Graph.py`: Graph representations (adjacency list and adjacency matrix) with various algorithms like BFS/DFS for pathfinding, connectivity checks, and topological sort (Kahn's algorithm).
    * `06b_Dijkstra.py`: Dijkstra's algorithm for shortest paths (versions for adjacency list and adjacency matrix).
* **7. Searching Algorithms** 🔍
    * `07_BinarySearch.py`: Binary Search (iterative and recursive versions).
* **8. Sorting Algorithms** 1️⃣2️⃣3️⃣
    * `08a_SelectionSort.py`: Selection Sort.
    * `08b_BubbleSort.py`: Bubble Sort (with optimization).
    * `08c_InsertionSort.py`: Insertion Sort.
    * `08d_ShellSort.py`: Shell Sort.
    * `08e_MergeSort.py`: Merge Sort.
    * `08f_QuickSort.py`: Quick Sort (Lomuto and Hoare partition scheme).
* **9. Disjoint Set** 📦📦 🍎🍎 📚📚
    * `09_UnionFind.py`: Union-Find data structure with path compression and union by rank optimizations.
* **10. Minimum Spanning Tree (MST) Algorithms** 🌳✨
    * `10_Kruskal_And_Prim.py`: Implementations of Kruskal's algorithm (typically for sparse graphs), Prim's algorithm using an adjacency matrix (suitable for dense graphs), and Prim's algorithm using an adjacency list (suitable for sparse graphs).

## 📐 Complexity Notation

Every method includes a one-line docstring with time and space complexity. The following variables are used:

| Variable | Meaning | Context |
|----------|---------|---------|
| `n` | Number of elements | General |
| `k` | Key length | Hash tables |
| `m` | Word / prefix length | Tries |
| `h` | Tree height | BSTs, heaps |
| `d` | Node depth | General trees |
| `V` | Number of vertices | Graphs |
| `E` | Number of edges | Graphs |
| `α(n)` | Inverse Ackermann function — grows so slowly it is effectively constant for all practical inputs | Union-Find |

**Conventions:**
* Unlabeled complexity is worst case (Big-O default). Only average/best cases are explicitly labeled (e.g., `O(n log n) avg, O(n^2) time`).
* Space complexity is auxiliary (excluding inputs/outputs) and includes the cost of called methods (e.g., a method calling a recursive `find()` inherits its stack usage).

## 🚀 How to Use

Requires **Python 3.10+** (PEP 604 `X | None`, PEP 585 `list[int]`). Each file includes inline tests via `assert` statements. Run any file directly — successful execution prints "All tests passed!":

```bash
python src/01a_HashTable_NoCollisionHandling.py
# Output: All tests passed!
```
