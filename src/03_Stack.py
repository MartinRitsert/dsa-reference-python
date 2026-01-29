from typing import Any
from collections import deque


# # Option 1: Using a list
# # This approach has a disadvantage: A list is a dynamic array. Thus,
# # for large stacks, it would copy many elements regularly
# class Stack:
#     def __init__(self) -> None:
#         self.container = []

#     def push(self, val: Any) -> None:
#         """Push an element onto the stack. O(1) amortized time."""
#         self.container.append(val)

#     def pop(self) -> Any:
#         """Remove and return the top element. O(1) amortized time."""
#         if not self.is_empty():
#             return self.container.pop()
#         raise IndexError("Stack is empty")

#     def peek(self) -> Any:
#         """Return the top element without removing it. O(1) time."""
#         if not self.is_empty():
#             return self.container[-1]
#         raise IndexError("Stack is empty")

#     def is_empty(self) -> bool:
#         """Check if the stack is empty. O(1) time."""
#         return len(self.container) == 0

#     def size(self) -> int:
#         """Return the number of elements. O(1) time."""
#         return len(self.container)


# # Option 2: Using a deque
# This is implemented using doubly linked lists and thus resolves
# the issue above (no copying of elements needed)
class Stack:
    def __init__(self) -> None:
        self.container = deque()

    # Sometimes called add
    def push(self, val: Any) -> None:
        """Push an element onto the stack. O(1) time."""
        self.container.append(val)

    # Sometimes called remove
    def pop(self) -> Any:
        """Remove and return the top element. O(1) time."""
        if not self.is_empty():
            return self.container.pop()
        raise IndexError("Stack is empty")

    def peek(self) -> Any:
        """Return the top element without removing it. O(1) time."""
        if not self.is_empty():
            return self.container[-1]
        raise IndexError("Stack is empty")

    def is_empty(self) -> bool:
        """Check if the stack is empty. O(1) time."""
        return len(self.container) == 0
        # More pythonic and thus preferred way is:
        # return not self.container

    def size(self) -> int:
        """Return the number of elements. O(1) time."""
        return len(self.container)


if __name__ == "__main__":
    stack = Stack()

    # Test empty stack
    assert stack.is_empty(), "New stack should be empty"
    assert stack.size() == 0, "New stack should have size 0"

    # Test push and peek
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert not stack.is_empty(), "Stack should not be empty after push"
    assert stack.size() == 3, "Stack should have size 3"
    assert stack.peek() == 3, "Peek should return last pushed element"

    # Test LIFO order
    assert stack.pop() == 3, "Pop should return 3"
    assert stack.pop() == 2, "Pop should return 2"
    assert stack.pop() == 1, "Pop should return 1"
    assert stack.is_empty(), "Stack should be empty after popping all"

    # Test error on empty pop/peek
    try:
        stack.pop()
        assert False, "Should raise IndexError on empty pop"
    except IndexError:
        pass

    try:
        stack.peek()
        assert False, "Should raise IndexError on empty peek"
    except IndexError:
        pass

    print("All tests passed!")
