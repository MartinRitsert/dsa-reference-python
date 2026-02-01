from typing import Optional, Any


class Node:
    def __init__(self, data: Any = None, next: Optional['Node'] = None, prev: Optional['Node'] = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

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
        node = Node(data, self.head, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data: Any) -> None:
        """Insert a node at the tail. O(1) time, O(1) space (tail pointer)."""
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def insert_at(self, index: int, data: Any) -> None:
        """Insert a node at a given index. O(n) time, O(1) space."""
        if index < 0 or index > self.get_length():
            raise IndexError("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
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
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                if node.next:
                    node.next.prev = node
                else:
                    self.tail = node
                return
            itr = itr.next
        raise ValueError(f"Value {data_after} not found in the list")

    def insert_values(self, data_list: list[Any]) -> None:
        """Replace the list with elements from data_list. O(m) time, O(1) space."""
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index: int) -> None:
        """Remove node at a given index. O(n) time, O(1) space."""
        if index < 0 or index >= self.get_length():
            raise IndexError("Invalid index")

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                else:
                    self.tail = itr.prev
                return
            itr = itr.next
            count += 1

    def remove_by_value(self, data: Any) -> None:
        """Remove first node with the given value. O(n) time, O(1) space."""
        if self.head is None:
            raise ValueError(f"Value {data} not found in the list")

        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        itr = self.head
        while itr:
            if itr.data == data:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                else:
                    self.tail = itr.prev
                return
            itr = itr.next
        raise ValueError(f"Value {data} not found in the list")

    def get_length(self) -> int:
        """Return the number of nodes. O(n) time, O(1) space."""
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print_forward(self) -> None:
        """Print all elements head to tail. O(n) time, O(n) space."""
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def print_backward(self) -> None:
        """Print all elements tail to head. O(n) time, O(n) space."""
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.tail
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev

        print(llstr)


if __name__ == '__main__':
    ll = DoublyLinkedList()

    # Test empty list
    assert ll.is_empty(), "New list should be empty"
    assert ll.get_length() == 0, "New list should have length 0"

    # Test insert_at_beginning
    ll.insert_at_beginning(1)
    assert ll.get_length() == 1, "Length should be 1"
    assert ll.find(1) == 0, "Should find 1 at index 0"
    assert ll.head == ll.tail, "Head and tail should be same for single element"

    # Test insert_at_end
    ll.insert_at_end(3)
    assert ll.get_length() == 2, "Length should be 2"
    assert ll.find(3) == 1, "Should find 3 at index 1"
    assert ll.tail.data == 3, "Tail should be 3"

    # Test insert_at
    ll.insert_at(1, 2)
    assert ll.get_length() == 3, "Length should be 3"
    assert ll.find(2) == 1, "Should find 2 at index 1"

    # Test insert_after_value
    ll.insert_after_value(2, 2.5)
    assert ll.find(2.5) == 2, "Should find 2.5 at index 2"

    # Test insert_values
    ll.insert_values([10, 20, 30])
    assert ll.get_length() == 3, "Length should be 3 after insert_values"
    assert ll.find(20) == 1, "Should find 20 at index 1"
    assert ll.head.data == 10, "Head should be 10"
    assert ll.tail.data == 30, "Tail should be 30"

    # Test remove_at
    ll.remove_at(1)
    assert ll.find(20) == -1, "20 should be removed"
    assert ll.get_length() == 2, "Length should be 2"

    # Test remove_by_value
    ll.insert_at_end(40)
    ll.remove_by_value(30)
    assert ll.find(30) == -1, "30 should be removed"
    assert ll.tail.data == 40, "Tail should be 40"

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