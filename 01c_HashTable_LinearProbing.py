from typing import Optional, Any

# NOTE: For simplicity in this manual implementation, we assume keys are strings
# to demonstrate a basic hashing algorithm. In a real-world hash table (like Python's dict),
# keys can be any hashable type (using Python's built-in hash() function).


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key: str, val: Any) -> None:
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)

    def __getitem__(self, key: str) -> Optional[Any]:
        h = self.get_hash(key)
        if self.arr[h] is None:
            return None
        prob_range = self.get_prob_range(h)

        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return None
            if element[0] == key:
                return element[1]
            
        return None
            
    def get_prob_range(self, index: int) -> list[int]:
        # The * operator unpacks the elements of the range object and 
        # the [] brackets create a new list containing these elements
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key: str, index: int) -> int:
        prob_range = self.get_prob_range(index)

        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
            
        raise Exception("Hashmap full")
    
    def __delitem__(self, key: str) -> None:
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)

        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None

                # Rehash elements that were inserted due to probing
                next_index = (prob_index + 1) % self.MAX

                while self.arr[next_index] is not None:
                    rehash_key, rehash_val = self.arr[next_index]
                    self.arr[next_index] = None
                    self.__setitem__(rehash_key, rehash_val)
                    next_index = (next_index + 1) % self.MAX
                    
                return