class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        # Inefficient for deep trees. In these cases, it's more efficient to
        # store the level in each tree node during construction
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = 3 * ' ' * self.get_level()
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def find(self, value):
        if self.data == value:
            return self
        for child in self.children:
            found = child.find(value)
            if found:
                return found
        return None
    
    def insert(self, parent_value, child_value):
        # If you already know the parent_node, you can skip find() and 
        # reduce insert() from O(n) to O(1)
        parent_node = self.find(parent_value)

        if parent_node:
            new_child = TreeNode(child_value)
            parent_node.add_child(new_child)
            return True
        
        return False
    
    def delete(self, value):
        node_to_delete = self.find(value)

        if node_to_delete and node_to_delete.parent:
            parent = node_to_delete.parent
            parent.children = [child for child in parent.children if child != node_to_delete]
            for child in node_to_delete.children:
                parent.add_child(child)
            return True
        
        return False
        

def build_product_tree():
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


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()

    print("\nFinding 'Mac':", root.find("Mac").data if root.find("Mac") else "Not found")
    print("Inserting 'Asus' under 'Laptop':", root.insert("Laptop", "Asus"))
    print("Deleting 'Surface':", root.delete("Surface"))
    root.print_tree()