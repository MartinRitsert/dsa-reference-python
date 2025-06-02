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