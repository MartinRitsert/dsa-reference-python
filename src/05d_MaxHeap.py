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
        """Insert an element and heapify up. O(log n) time."""
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
        while (self.maxheap[index] > self.maxheap[parent] and index > 1):
            self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2

    def peek(self) -> Any:
        """Return the maximum element without removing it. O(1) time."""
        if self.real_size < 1:
            raise IndexError("Heap is empty!")
        return self.maxheap[1]

    def pop(self) -> Any:
        """Remove and return the maximum element, then heapify down. O(log n) time."""
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
        """Return the number of elements. O(1) time."""
        return self.real_size

    def __str__(self) -> str:
        return str(self.maxheap[1:self.real_size+1])


if __name__ == "__main__":
    maxHeap = MaxHeap(5)

    # Test empty heap
    assert maxHeap.size() == 0, "New heap should have size 0"

    # Test add and peek
    maxHeap.add(3)
    maxHeap.add(1)
    maxHeap.add(2)
    assert maxHeap.size() == 3, "Heap should have size 3"
    assert maxHeap.peek() == 3, "Max element should be 3"

    # Test pop returns elements in descending order
    assert maxHeap.pop() == 3, "First pop should return 3"
    assert maxHeap.pop() == 2, "Second pop should return 2"
    assert maxHeap.pop() == 1, "Third pop should return 1"
    assert maxHeap.size() == 0, "Heap should be empty after popping all"

    # Test add after empty
    maxHeap.add(4)
    maxHeap.add(5)
    assert maxHeap.peek() == 5, "Max should be 5"
    assert maxHeap.size() == 2, "Heap should have size 2"

    # Test error on empty pop/peek
    maxHeap.pop()
    maxHeap.pop()
    try:
        maxHeap.pop()
        assert False, "Should raise IndexError on empty pop"
    except IndexError:
        pass

    try:
        maxHeap.peek()
        assert False, "Should raise IndexError on empty peek"
    except IndexError:
        pass

    # Test overflow
    fullHeap = MaxHeap(2)
    fullHeap.add(1)
    fullHeap.add(2)
    try:
        fullHeap.add(3)
        assert False, "Should raise OverflowError when heap is full"
    except OverflowError:
        pass

    print("All tests passed!")