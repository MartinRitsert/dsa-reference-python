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
        self.real_size += 1

        # Print error message if number of elements in Heap > preset heap_size
        if self.real_size > self.heap_size:
            print("Added too many elements!")
            self.real_size -= 1
            return

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
            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            index = parent
            parent = index // 2

    def peek(self) -> Any:
        return self.minheap[1]

    def pop(self) -> Any:
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
            self.minheap[index], self.minheap[smallest] = self.minheap[smallest], self.minheap[index]
            index = smallest

        return removed

    def size(self) -> int:
        return self.real_size

    def __str__(self) -> str:
        return str(self.minheap[1:self.real_size+1])


if __name__ == "__main__":
    # Test cases
    minHeap = MinHeap(5)
    minHeap.add(3)
    minHeap.add(1)
    minHeap.add(2)
    print(minHeap)
    # [1,3,2]
    print(minHeap.peek())
    # 1
    print(minHeap.pop())
    # 1
    print(minHeap.pop())
    # 2
    print(minHeap.pop())
    # 3
    minHeap.add(4)
    minHeap.add(5)
    print(minHeap)
    # [4,5]