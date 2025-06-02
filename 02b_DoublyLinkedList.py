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
        itr = self.head

        index = 0
        while itr:
            if itr.data == data:
                return index
            
            itr = itr.next
            index += 1

        return -1

    def is_empty(self) -> bool:
        return self.head is None

    def insert_at_beginning(self, data: Any) -> None:
        node = Node(data, self.head, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data: Any) -> None:
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def insert_at(self, index: int, data: Any) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
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
        if self.head is None:
            return

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
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index: int) -> None:
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

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
        if self.head is None:
            return

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
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print_forward(self) -> None:
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