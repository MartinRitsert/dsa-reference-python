from typing import Optional, Any

# NOTE: For simplicity in this manual implementation, we assume keys are strings
# to demonstrate a basic hashing algorithm. In a real-world hash table (like Python's dict),
# keys can be any hashable type (using Python's built-in hash() function).


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key: str, val: Any) -> None:
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                return
        self.arr[h].append((key, val))

    def __getitem__(self, key: str) -> Optional[Any]:
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None
    
    def __delitem__(self, key: str) -> None:
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]