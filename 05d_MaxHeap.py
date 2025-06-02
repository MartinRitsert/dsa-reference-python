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
        self.real_size += 1

        # Print error message if number of elements in Heap > preset heap_size
        if self.real_size > self.heap_size:
            print("Added too many elements!")
            self.real_size -= 1
            return

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
        return self.maxheap[1]

    def pop(self) -> Any:
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

            # Swap the current node with the smallest child
            self.maxheap[index], self.maxheap[largest] = self.maxheap[largest], self.maxheap[index]
            index = largest

        return removed

    def size(self) -> int:
        return self.real_size

    def __str__(self) -> str:
        return str(self.maxheap[1:self.real_size+1])


if __name__ == "__main__":
    # Test cases
    maxHeap = MaxHeap(5)
    maxHeap.add(3)
    maxHeap.add(1)
    maxHeap.add(2)
    print(maxHeap)
    # [3,1,2]
    print(maxHeap.peek())
    # 3
    print(maxHeap.pop())
    # 3
    print(maxHeap.pop())
    # 2
    print(maxHeap.pop())
    # 1
    maxHeap.add(4)
    maxHeap.add(5)
    print(maxHeap)
    # [5,4]