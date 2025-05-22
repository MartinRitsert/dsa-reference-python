from collections import deque


# # Option 1: Using a list
# # This approach has a disadvantage: A list is a dynamic array. Thus, 
# # for large stacks, it would copy many elements regularly
# class Stack:
#     def __init__(self):
#         self.container = [] 

#     def push(self, val):
#         self.container.append(val)

#     def pop(self):
#         if not self.is_empty():
#             return self.container.pop()
#         raise IndexError("Stack is empty")
    
#     def peek(self):
#         if not self.is_empty():
#             return self.container[-1]
#         raise IndexError("Stack is empty")

#     def is_empty(self):
#         return len(self.container) == 0
    
#     def size(self):
#         return len(self.container)
    

# # Option 2: Using a deque
# This is implemented using doubly linked lists and thus resolves 
# the issue above (no copying of elements needed)
class Stack:
    def __init__(self):
        self.container = deque()

    # Sometimes called add
    def push(self, val):
        self.container.append(val)

    # Sometimes called remove
    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.container) == 0
        # More pythonic and thus preferred way is:
        # return not self.container
    
    def size(self):
        return len(self.container)