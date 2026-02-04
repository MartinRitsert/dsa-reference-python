from __future__ import annotations

from typing import Any


class MaxHeap:
    def __init__(self, heap_size: int) -> None:
        # Create a complete binary tree using an array
        # Then, use the binary tree to construct a Heap
        self.heap_size = heap_size
        self.maxheap = [0] * (heap_size + 1)
        # real_size records the number of elements in the heap
        self.real_size = 0

    def add(self, element: Any) -> None:
        """Insert an element and heapify up. O(log n) time, O(1) space."""
        self.real_size += 1

        if self.real_size > self.heap_size:
            self.real_size -= 1
            raise OverflowError("Heap is full")

        # Add the element into the array
        self.maxheap[self.real_size] = element

        # Index of the newly added element
        index = self.real_size

        # Parent node of the newly added element
        # Root is stored at node with index 1
        # Index of the parent of any node is [index // 2]
        # Index of the left child is [index * 2]
        # Index of the right child is [index * 2 + 1]
        parent = index // 2

        # If the newly added element is larger than its parent node,
        # its value will be exchanged with that of the parent node
        # This is called "heapify up"
        while self.maxheap[index] > self.maxheap[parent] and index > 1:
            self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2

    def peek(self) -> Any:
        """Return the maximum element without removing it. O(1) time, O(1) space."""
        if self.real_size < 1:
            raise IndexError("Heap is empty!")
        return self.maxheap[1]

    def pop(self) -> Any:
        """Remove and return the maximum element, then heapify down. O(log n) time, O(1) space."""
        if self.real_size < 1:
            raise IndexError("Heap is empty!")

        removed = self.maxheap[1]

        # Put the last element in the Heap to the top of Heap
        self.maxheap[1] = self.maxheap[self.real_size]
        
        # Remove element implicitly by decreasing real_size
        self.real_size -= 1

        # Heapify down
        index = 1
        while index <= self.real_size // 2:
            left = index * 2
            right = index * 2 + 1
            largest = index 

            if left <= self.real_size and self.maxheap[left] > self.maxheap[largest]:
                largest = left
            
            if right <= self.real_size and self.maxheap[right] > self.maxheap[largest]:
                largest = right
            
            # Heap property is satisfied for this subtree, no more swaps needed
            if largest == index:
                break

            # Swap the current node with the largest child
            self.maxheap[index], self.maxheap[largest] = self.maxheap[largest], self.maxheap[index]
            index = largest

        return removed

    def size(self) -> int:
        """Return the number of elements. O(1) time, O(1) space."""
        return self.real_size

    def __str__(self) -> str:
        return str(self.maxheap[1:self.real_size+1])


if __name__ == "__main__":
    max_heap = MaxHeap(5)

    # Test empty heap
    assert max_heap.size() == 0, "New heap should have size 0"

    # Test add and peek
    max_heap.add(3)
    max_heap.add(1)
    max_heap.add(2)
    assert max_heap.size() == 3, "Heap should have size 3"
    assert max_heap.peek() == 3, "Max element should be 3"

    # Test pop returns elements in descending order
    assert max_heap.pop() == 3, "First pop should return 3"
    assert max_heap.pop() == 2, "Second pop should return 2"
    assert max_heap.pop() == 1, "Third pop should return 1"
    assert max_heap.size() == 0, "Heap should be empty after popping all"

    # Test add after empty
    max_heap.add(4)
    max_heap.add(5)
    assert max_heap.peek() == 5, "Max should be 5"
    assert max_heap.size() == 2, "Heap should have size 2"

    # Test error on empty pop/peek
    max_heap.pop()
    max_heap.pop()
    try:
        max_heap.pop()
        assert False, "Should raise IndexError on empty pop"
    except IndexError:
        pass

    try:
        max_heap.peek()
        assert False, "Should raise IndexError on empty peek"
    except IndexError:
        pass

    # Test with negative numbers
    neg_heap = MaxHeap(5)
    neg_heap.add(-3)
    neg_heap.add(1)
    neg_heap.add(-5)
    neg_heap.add(2)
    assert neg_heap.pop() == 2, "Max should be 2"
    assert neg_heap.pop() == 1, "Next max should be 1"
    assert neg_heap.pop() == -3, "Next max should be -3"
    assert neg_heap.pop() == -5, "Next max should be -5"

    # Test with duplicates
    dup_heap = MaxHeap(5)
    dup_heap.add(3)
    dup_heap.add(1)
    dup_heap.add(3)
    dup_heap.add(1)
    assert dup_heap.pop() == 3, "First pop should be 3"
    assert dup_heap.pop() == 3, "Second pop should be 3"
    assert dup_heap.pop() == 1, "Third pop should be 1"
    assert dup_heap.pop() == 1, "Fourth pop should be 1"

    # Test overflow
    full_heap = MaxHeap(2)
    full_heap.add(1)
    full_heap.add(2)
    try:
        full_heap.add(3)
        assert False, "Should raise OverflowError when heap is full"
    except OverflowError:
        pass

    print("All tests passed!")