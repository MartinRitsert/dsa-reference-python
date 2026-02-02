from typing import Optional, Any


class Node:
    def __init__(self, data: Any = None, next: Optional['Node']= None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def find(self, data: Any) -> int:
        """Return index of first occurrence, or -1 if not found. O(n) time, O(1) space."""
        itr = self.head

        index = 0
        while itr:
            if itr.data == data:
                return index
            
            itr = itr.next
            index += 1

        return -1

    def is_empty(self) -> bool:
        """Check if the list is empty. O(1) time, O(1) space."""
        return self.head is None

    def insert_at_beginning(self, data: Any) -> None:
        """Insert a node at the head. O(1) time, O(1) space."""
        node = Node(data, self.head)
        self.head = node
        self.length += 1

    def insert_at_end(self, data: Any) -> None:
        """Insert a node at the tail. O(n) time, O(1) space."""
        if self.head is None:
            self.head = Node(data, None)
            self.length += 1
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
        self.length += 1

    def insert_at(self, index: int, data: Any) -> None:
        """Insert a node at a given index. O(n) time, O(1) space."""
        if index < 0 or index > self.length:
            raise IndexError("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                self.length += 1
                return

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after: Any, data_to_insert: Any) -> None:
        """Insert a node after the first occurrence of a value. O(n) time, O(1) space."""
        if self.head is None:
            raise ValueError(f"Value {data_after} not found in the list")

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                self.length += 1
                return
            itr = itr.next
        raise ValueError(f"Value {data_after} not found in the list")

    def replace_with_list(self, data_list: list[Any]) -> None:
        """Replace the list with elements from data_list. O(m) time, O(1) space."""
        self.head = None
        self.length = 0
        tail = None
        for data in data_list:
            node = Node(data)
            if tail is None:
                self.head = node
            else:
                tail.next = node
            tail = node
            self.length += 1

    def remove_at(self, index: int) -> None:
        """Remove node at a given index. O(n) time, O(1) space."""
        if index < 0 or index >= self.length:
            raise IndexError("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                self.length -= 1
                return

            itr = itr.next
            count += 1

    def remove_by_value(self, data: Any) -> None:
        """Remove first node with the given value. O(n) time, O(1) space."""
        if self.head is None:
            raise ValueError(f"Value {data} not found in the list")

        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                self.length -= 1
                return
            itr = itr.next

        raise ValueError(f"Value {data} not found in the list")

    def get_length(self) -> int:
        """Return the number of nodes. O(1) time, O(1) space."""
        return self.length

    def print(self) -> None:
        """Print all elements as a string. O(n) time, O(n) space."""
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        parts = []

        while itr:
            parts.append(str(itr.data))
            itr = itr.next

        print('-->'.join(parts))


if __name__ == '__main__':
    ll = LinkedList()

    # Test empty list
    assert ll.is_empty(), "New list should be empty"
    assert ll.get_length() == 0, "New list should have length 0"

    # Test insert_at_beginning
    ll.insert_at_beginning(1)
    assert ll.get_length() == 1, "Length should be 1"
    assert ll.find(1) == 0, "Should find 1 at index 0"

    # Test insert_at_end
    ll.insert_at_end(3)
    assert ll.get_length() == 2, "Length should be 2"
    assert ll.find(3) == 1, "Should find 3 at index 1"

    # Test insert_at
    ll.insert_at(1, 2)
    assert ll.get_length() == 3, "Length should be 3"
    assert ll.find(2) == 1, "Should find 2 at index 1"

    # Test insert_after_value
    ll.insert_after_value(2, 2.5)
    assert ll.find(2.5) == 2, "Should find 2.5 at index 2"

    # Test replace_with_list
    ll.replace_with_list([10, 20, 30])
    assert ll.get_length() == 3, "Length should be 3 after replace_with_list"
    assert ll.find(20) == 1, "Should find 20 at index 1"

    # Test remove_at
    ll.remove_at(1)
    assert ll.find(20) == -1, "20 should be removed"
    assert ll.get_length() == 2, "Length should be 2"

    # Test remove_by_value
    ll.insert_at_end(40)
    ll.remove_by_value(30)
    assert ll.find(30) == -1, "30 should be removed"

    # Test error handling
    try:
        ll.insert_at(100, 999)
        assert False, "Should raise IndexError for invalid index"
    except IndexError:
        pass

    try:
        ll.remove_at(-1)
        assert False, "Should raise IndexError for negative index"
    except IndexError:
        pass

    try:
        ll.remove_by_value(999)
        assert False, "Should raise ValueError for non-existent value"
    except ValueError:
        pass

    print("All tests passed!")