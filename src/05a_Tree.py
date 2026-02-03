from __future__ import annotations

from typing import Any


class TreeNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child: TreeNode) -> None:
        """Add a child node. O(1) time, O(1) space."""
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        """Return the depth of this node. O(d) time, O(1) space."""
        # Can be optimized to O(1) by storing the level in each node during construction.
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level: int = 0) -> None:
        """Print the tree with indentation by level. O(n) time, O(h) space."""
        spaces = 3 * " " * level
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        for child in self.children:
            child.print_tree(level + 1)

    def find(self, value: Any) -> TreeNode | None:
        """Search for a value in the tree. O(n) time, O(h) space."""
        if self.data == value:
            return self
        for child in self.children:
            found = child.find(value)
            if found:
                return found
        return None

    def insert(self, parent_value: Any, child_value: Any) -> bool:
        """Insert a child under the node with parent_value. O(n) time, O(h) space."""
        # If you already know the parent_node, you can skip find() and
        # reduce insert() from O(n) to O(1)
        parent_node = self.find(parent_value)

        if parent_node:
            new_child = TreeNode(child_value)
            parent_node.add_child(new_child)
            return True

        return False

    def delete(self, value: Any) -> bool:
        """Delete a node and re-parent its children. O(n) time, O(h) space."""
        node_to_delete = self.find(value)

        if node_to_delete and node_to_delete.parent:
            parent = node_to_delete.parent
            parent.children = [
                child for child in parent.children if child != node_to_delete
            ]
            for child in node_to_delete.children:
                parent.add_child(child)
            return True

        return False


def build_product_tree() -> TreeNode:
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Samsung Galaxy"))

    root.add_child(laptop)
    root.add_child(cellphone)

    return root


if __name__ == "__main__":
    root = build_product_tree()

    # Test find
    assert root.find("Mac") is not None, "Should find 'Mac'"
    assert root.find("Mac").data == "Mac", "Found node should have data 'Mac'"
    assert root.find("NonExistent") is None, "Should not find 'NonExistent'"

    # Test get_level
    assert root.get_level() == 0, "Root should be at level 0"
    assert root.find("Laptop").get_level() == 1, "Laptop should be at level 1"
    assert root.find("Mac").get_level() == 2, "Mac should be at level 2"

    # Test insert
    assert root.insert("Laptop", "Asus"), "Should insert 'Asus' under 'Laptop'"
    assert root.find("Asus") is not None, "Should find inserted 'Asus'"
    assert root.find("Asus").parent.data == "Laptop", "Asus parent should be Laptop"
    assert not root.insert("NonExistent", "Test"), (
        "Should fail to insert under non-existent parent"
    )

    # Test delete
    assert root.delete("Surface"), "Should delete 'Surface'"
    assert root.find("Surface") is None, "Should not find deleted 'Surface'"
    assert not root.delete("NonExistent"), "Should fail to delete non-existent node"

    # Test cannot delete root (no parent)
    assert not root.delete("Electronics"), "Should not be able to delete root"

    print("All tests passed!")
