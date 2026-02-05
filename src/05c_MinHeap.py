from __future__ import annotations

from typing import Any


class MinHeap:
    def __init__(self, heap_size: int) -> None:
        # Create a complete binary tree using an array
        # Then, use the binary tree to construct a Heap
        self.heap_size = heap_size
        self.minheap = [0] * (heap_size + 1)
        # real_size records the number of elements in the heap
        self.real_size = 0

    def add(self, element: Any) -> None:
        """Insert an element and heapify up. O(log n) time, O(1) space."""
        self.real_size += 1

        if self.real_size > self.heap_size:
            self.real_size -= 1
            raise OverflowError("Heap is full")

        # Add the element into the array
        self.minheap[self.real_size] = element

        # Index of the newly added element
        index = self.real_size

        # Parent node of the newly added element
        # Root is stored at node with index 1
        # Index of the parent of any node is [index // 2]
        # Index of the left child is [index * 2]
        # Index of the right child is [index * 2 + 1]
        parent = index // 2

        # If the newly added element is smaller than its parent node,
        # its value will be exchanged with that of the parent node
        # This is called "heapify up"
        while self.minheap[index] < self.minheap[parent] and index > 1:
            self.minheap[parent], self.minheap[index] = (
                self.minheap[index],
                self.minheap[parent],
            )
            index = parent
            parent = index // 2

    def peek(self) -> Any:
        """Return the minimum element without removing it. O(1) time, O(1) space."""
        if self.real_size < 1:
            raise IndexError("Heap is empty!")
        return self.minheap[1]

    def pop(self) -> Any:
        """Remove and return the minimum element, then heapify down. O(log n) time, O(1) space."""
        if self.real_size < 1:
            raise IndexError("Heap is empty!")

        removed = self.minheap[1]

        # Put the last element in the Heap to the top of Heap
        self.minheap[1] = self.minheap[self.real_size]

        # Remove element implicitly by decreasing real_size
        self.real_size -= 1

        # Heapify down
        index = 1
        while index <= self.real_size // 2:
            left = index * 2
            right = index * 2 + 1
            smallest = index

            if left <= self.real_size and self.minheap[left] < self.minheap[smallest]:
                smallest = left

            if right <= self.real_size and self.minheap[right] < self.minheap[smallest]:
                smallest = right

            # Heap property is satisfied for this subtree, no more swaps needed
            if smallest == index:
                break

            # Swap the current node with the smallest child
            self.minheap[index], self.minheap[smallest] = (
                self.minheap[smallest],
                self.minheap[index],
            )
            index = smallest

        return removed

    def size(self) -> int:
        """Return the number of elements. O(1) time, O(1) space."""
        return self.real_size

    def __str__(self) -> str:
        return str(self.minheap[1 : self.real_size + 1])


if __name__ == "__main__":
    min_heap = MinHeap(5)

    # Test empty heap
    assert min_heap.size() == 0, "New heap should have size 0"

    # Test add and peek
    min_heap.add(3)
    min_heap.add(1)
    min_heap.add(2)
    assert min_heap.size() == 3, "Heap should have size 3"
    assert min_heap.peek() == 1, "Min element should be 1"

    # Test pop returns elements in ascending order
    assert min_heap.pop() == 1, "First pop should return 1"
    assert min_heap.pop() == 2, "Second pop should return 2"
    assert min_heap.pop() == 3, "Third pop should return 3"
    assert min_heap.size() == 0, "Heap should be empty after popping all"

    # Test add after empty
    min_heap.add(4)
    min_heap.add(5)
    assert min_heap.peek() == 4, "Min should be 4"
    assert min_heap.size() == 2, "Heap should have size 2"

    # Test error on empty pop/peek
    min_heap.pop()
    min_heap.pop()
    try:
        min_heap.pop()
        assert False, "Should raise IndexError on empty pop"
    except IndexError:
        pass

    try:
        min_heap.peek()
        assert False, "Should raise IndexError on empty peek"
    except IndexError:
        pass

    # Test with negative numbers
    neg_heap = MinHeap(5)
    neg_heap.add(-3)
    neg_heap.add(1)
    neg_heap.add(-5)
    neg_heap.add(2)
    assert neg_heap.pop() == -5, "Min should be -5"
    assert neg_heap.pop() == -3, "Next min should be -3"
    assert neg_heap.pop() == 1, "Next min should be 1"
    assert neg_heap.pop() == 2, "Next min should be 2"

    # Test with duplicates
    dup_heap = MinHeap(5)
    dup_heap.add(3)
    dup_heap.add(1)
    dup_heap.add(3)
    dup_heap.add(1)
    assert dup_heap.pop() == 1, "First pop should be 1"
    assert dup_heap.pop() == 1, "Second pop should be 1"
    assert dup_heap.pop() == 3, "Third pop should be 3"
    assert dup_heap.pop() == 3, "Fourth pop should be 3"

    # Test overflow
    full_heap = MinHeap(2)
    full_heap.add(1)
    full_heap.add(2)
    try:
        full_heap.add(3)
        assert False, "Should raise OverflowError when heap is full"
    except OverflowError:
        pass

    print("All tests passed!")
