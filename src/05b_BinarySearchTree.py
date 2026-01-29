from typing import Optional, Any

# The pre_order, in_order, and post_order algorithms are
# valid not only for BSTs but for any binary tree. For BSTs,
# the outputs of in-order traversal will always be sorted.


class BinarySearchTreeNode:
    def __init__(
        self,
        data: Any,
        left: Optional["BinarySearchTreeNode"] = None,
        right: Optional["BinarySearchTreeNode"] = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    # # Recursive approach (inefficient for deep trees):
    # def add_child(self, data: Any) -> None:
    #     """Insert a value into the BST. O(h) time, O(h) space (call stack)."""
    #     if data == self.data:
    #         return
    #
    #     if data < self.data:
    #         if self.left:
    #             self.left.add_child(data)
    #         else:
    #             self.left = BinarySearchTreeNode(data)
    #     else:
    #         if self.right:
    #             self.right.add_child(data)
    #         else:
    #             self.right = BinarySearchTreeNode(data)

    # Iterative approach (efficient for deep trees):
    def add_child(self, data: Any) -> None:
        """Insert a value into the BST. O(h) time, where h is tree height."""
        current = self

        while current:
            if data == current.data:
                return
            elif data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTreeNode(data)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BinarySearchTreeNode(data)
                    return

    # # Recursive approach (inefficient for deep trees):
    # def search(self, val: Any) -> bool:
    #     """Search for a value in the BST. O(h) time, O(h) space (call stack)."""
    #     if self.data == val:
    #         return True

    #     elif val < self.data:
    #         if self.left:
    #             return self.left.search(val)
    #         else:
    #             return False

    #     else:
    #         if self.right:
    #             return self.right.search(val)
    #         else:
    #             return False

    # Iterative approach (efficient for deep trees):
    def search(self, val: Any) -> bool:
        """Search for a value in the BST. O(h) time, where h is tree height."""
        current = self

        while current:
            if val == current.data:
                return True
            elif val < current.data:
                current = current.left
            else:
                current = current.right

        return False

    # # Recursive approach (inefficient for deep trees):
    # def in_order_traversal(self) -> list[Any]:
    #     """Return elements in sorted order (left, root, right). O(n) time, O(h) space."""
    #     elements = []

    #     if self.left:
    #         elements.extend(self.left.in_order_traversal())

    #     elements.append(self.data)

    #     if self.right:
    #         elements.extend(self.right.in_order_traversal())

    #     return elements

    # Iterative approach (efficient for deep trees):
    def in_order_traversal(self) -> list[Any]:
        """Return elements in sorted order (left, root, right). O(n) time."""
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
    # def pre_order_traversal(self) -> list[Any]:
    #     """Return elements in pre-order (root, left, right). O(n) time, O(h) space."""
    #     elements = [self.data]

    #     if self.left:
    #         elements.extend(self.left.pre_order_traversal())

    #     if self.right:
    #         elements.extend(self.right.pre_order_traversal())

    #     return elements

    # Iterative approach (efficient for deep trees):
    def pre_order_traversal(self) -> list[Any]:
        """Return elements in pre-order (root, left, right). O(n) time."""
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
    # def post_order_traversal(self) -> list[Any]:
    #     """Return elements in post-order (left, right, root). O(n) time, O(h) space."""
    #     elements = []

    #     if self.left:
    #         elements.extend(self.left.post_order_traversal())

    #     if self.right:
    #         elements.extend(self.right.post_order_traversal())

    #     elements.append(self.data)

    #     return elements

    # Iterative approach (efficient for deep trees):
    def post_order_traversal(self) -> list[Any]:
        """Return elements in post-order (left, right, root). O(n) time."""
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
    # # Alternative to previous post_order_traversal that uses a visited
    # # flag and prevents the need to reverse the list at the end:
    # def post_order_traversal(self) -> list[Any]:
    #     """Return elements in post-order (left, right, root). O(n) time."""
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

    # # Recursive approach (inefficient for deep trees):
    # def find_min(self) -> Any:
    #     """Return the minimum value. O(h) time, O(h) space (call stack)."""
    #     if self.left is None:
    #         return self.data
    #     return self.left.find_min()

    # Iterative approach (efficient for deep trees):
    def find_min(self) -> Any:
        """Return the minimum value. O(h) time, where h is tree height."""
        current = self
        while current.left:
            current = current.left
        return current.data

    # # Recursive approach (inefficient for deep trees):
    # def find_max(self) -> Any:
    #     """Return the maximum value. O(h) time, O(h) space (call stack)."""
    #     if self.right is None:
    #         return self.data
    #     return self.right.find_max()

    # Iterative approach (efficient for deep trees):
    def find_max(self) -> Any:
        """Return the maximum value. O(h) time, where h is tree height."""
        current = self
        while current.right:
            current = current.right
        return current.data

    # # Recursive approach (inefficient for deep trees):
    # For deep trees, this can be optimized using the iterative
    # [Pre-order/Post-order] traversal patterns documented above.
    def calculate_sum(self) -> Any:
        """Return the sum of all values. O(n) time."""
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return left_sum + right_sum + self.data

    def delete(self, val: Any) -> Optional["BinarySearchTreeNode"]:
        """Delete a value and return the new subtree root. O(h) time."""
        # IMPORTANT: This method does not mutate the caller's reference.
        # Example: root = root.delete(value)
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements: list[Any]) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 24]
    numbers_tree = build_tree(numbers)

    # Test in_order_traversal (should be sorted for BST)
    in_order = numbers_tree.in_order_traversal()
    assert in_order == sorted(numbers), "In-order traversal should be sorted"

    # Test pre_order_traversal
    pre_order = numbers_tree.pre_order_traversal()
    assert pre_order[0] == 17, "Pre-order should start with root"
    assert len(pre_order) == len(numbers), "Pre-order should have all elements"

    # Test post_order_traversal
    post_order = numbers_tree.post_order_traversal()
    assert post_order[-1] == 17, "Post-order should end with root"
    assert len(post_order) == len(numbers), "Post-order should have all elements"

    # Test search
    assert numbers_tree.search(20), "Should find 20"
    assert numbers_tree.search(17), "Should find root 17"
    assert not numbers_tree.search(21), "Should not find 21"
    assert not numbers_tree.search(100), "Should not find 100"

    # Test find_min and find_max
    assert numbers_tree.find_min() == 1, "Min should be 1"
    assert numbers_tree.find_max() == 24, "Max should be 24"

    # Test calculate_sum
    assert numbers_tree.calculate_sum() == sum(numbers), "Sum should match"

    # Test delete
    numbers_tree = numbers_tree.delete(20)
    assert not numbers_tree.search(20), "Should not find deleted 20"
    assert numbers_tree.search(23), "Should still find 23 after deleting 20"

    # Test delete leaf
    numbers_tree = numbers_tree.delete(1)
    assert not numbers_tree.search(1), "Should not find deleted 1"

    print("All tests passed!")
