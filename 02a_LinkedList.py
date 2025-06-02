from typing import Optional, Any


class Node:
    def __init__(self, data: Any = None, next: Optional['Node']= None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

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
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index: int, data: Any) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after: Any, data_to_insert: Any) -> None:
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return
            itr = itr.next
        raise ValueError(f"Value {data_after} not found in the list")

    def insert_values(self, data_list: list[Any]) -> None:
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index: int) -> None:
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next 
                break

            itr = itr.next
            count += 1

    def remove_by_value(self, data: Any) -> None:
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def get_length(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print(self) -> None:
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        # Could also optimize by making llstr a list and then 
        # joining the list into a single string in the end
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()