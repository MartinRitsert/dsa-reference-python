class BinarySearchTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True
        
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # # Recursive approach (inefficient for deep trees):
    # def in_order_traversal(self):
    #     elements = []

    #     if self.left:
    #         elements.extend(self.left.in_order_traversal())

    #     elements.append(self.data)

    #     if self.right:
    #         elements.extend(self.right.in_order_traversal())

    #     return elements

    # Iterative approach (efficient for deep trees):
    def in_order_traversal(self):
        elements = []
        stack = []

        curr = self
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                elements.append(curr.data)
                curr = curr.right

        return elements

    # # Recursive approach (inefficient for deep trees):
    # def pre_order_traversal(self):
    #     elements = [self.data]

    #     if self.left:
    #         elements.extend(self.left.pre_order_traversal())

    #     if self.right:
    #         elements.extend(self.right.pre_order_traversal())

    #     return elements

    # Iterative approach (efficient for deep trees):
    def pre_order_traversal(self):
        elements = []
        stack = [self]

        while stack:
            curr = stack.pop()
            elements.append(curr.data)

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)

        return elements

    # # Recursive approach (inefficient for deep trees):
    # def post_order_traversal(self):
    #     elements = []

    #     if self.left:
    #         elements.extend(self.left.post_order_traversal())

    #     if self.right:
    #         elements.extend(self.right.post_order_traversal())

    #     elements.append(self.data)

    #     return elements

    # Iterative approach (efficient for deep trees):
    def post_order_traversal(self):
        elements = []
        stack = [self]

        while stack:
            curr = stack.pop()
            elements.append(curr.data)

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return elements[::-1]
    
    # # Iterative approach (efficient for deep trees):
    # # Alternative to previous post_order_traversal that uses a visited flag and prevents the need to reverse the list at the end:
    # def post_order_traversal(self):
    #     elements = []
    #     stack = [(self, False)]

    #     while stack:
    #         curr, visited = stack.pop()
    #         if not curr:
    #             continue
    #         if visited:
    #             elements.append(curr.data)
    #         else:
    #             stack.append((curr, True))
    #             stack.append((curr.right, False))
    #             stack.append((curr.left, False))

    #     return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return left_sum + right_sum + self.data
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
        

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 24]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.search(21))
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())
