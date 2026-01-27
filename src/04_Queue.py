from typing import Any
from collections import deque


# # Option 1: Using a list
# # This approach has a disadvantage: A list is a dynamic array. Thus,
# # for large queues, it would copy many elements regularly
# class Queue:
#     def __init__(self) -> None:
#         self.container = []

#     def put(self, val: Any) -> None:
#         self.container.append(val)

#     def get(self) -> Any:
#         if not self.is_empty():
#             return self.container.pop(0)
#         raise IndexError("Queue is empty")

#     def peek(self) -> Any:
#         if not self.is_empty():
#             return self.container[0]
#         raise IndexError("Queue is empty")

#     def is_empty(self) -> bool:
#         return len(self.container) == 0

#     def size(self) -> int:
#         return len(self.container)


# # Option 2: Using a deque
# This is implemented using doubly linked lists and thus resolves
# the issue above (no copying of elements needed)
class Queue:
    def __init__(self) -> None:
        self.container = deque()

    # Sometimes called enqueue or add
    def put(self, val: Any) -> None:
        self.container.append(val)

    # Sometimes called dequeue or remove
    def get(self) -> Any:
        if not self.is_empty():
            return self.container.popleft()
        raise IndexError("Queue is empty")

    def peek(self) -> Any:
        if not self.is_empty():
            return self.container[0]
        raise IndexError("Queue is empty")

    def is_empty(self) -> bool:
        return len(self.container) == 0
        # More pythonic and thus preferred way is:
        # return not self.container

    def size(self) -> int:
        return len(self.container)


if __name__ == "__main__":
    queue = Queue()

    # Test empty queue
    assert queue.is_empty(), "New queue should be empty"
    assert queue.size() == 0, "New queue should have size 0"

    # Test put and peek
    queue.put(1)
    queue.put(2)
    queue.put(3)
    assert not queue.is_empty(), "Queue should not be empty after put"
    assert queue.size() == 3, "Queue should have size 3"
    assert queue.peek() == 1, "Peek should return first element"

    # Test FIFO order
    assert queue.get() == 1, "Get should return 1"
    assert queue.get() == 2, "Get should return 2"
    assert queue.get() == 3, "Get should return 3"
    assert queue.is_empty(), "Queue should be empty after getting all"

    # Test error on empty get/peek
    try:
        queue.get()
        assert False, "Should raise IndexError on empty get"
    except IndexError:
        pass

    try:
        queue.peek()
        assert False, "Should raise IndexError on empty peek"
    except IndexError:
        pass

    print("All tests passed!")
