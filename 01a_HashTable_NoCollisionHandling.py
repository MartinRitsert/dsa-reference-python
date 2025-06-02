from typing import Optional, Any

# IMPORTANT: Does not handle hash collisions

# NOTE: For simplicity in this manual implementation, we assume keys are strings
# to demonstrate a basic hashing algorithm. In a real-world hash table (like Python's dict),
# keys can be any hashable type (using Python's built-in hash() function),
# and robust collision resolution is critical.


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    # def add(self, key: str, val: Any) -> None:
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    # def get(self, key: str) -> Any:
    #     h = self.get_hash(key)
    #     return self.arr[h]
    
    # To be able to use my_array[key] = value instead of my_array.add(key, value),
    # we can overwrite the __setitem__ operator
    def __setitem__(self, key: str, val: Any) -> None:
        h = self.get_hash(key)
        self.arr[h] = val

    # To be able to use my_array[key] instead of my_array.get(key),
    # we can overwrite the __getitem__ operator
    def __getitem__(self, key: str) -> Optional[Any]:
        h = self.get_hash(key)
        return self.arr[h]
    
    # Can also overwrite the __delitem__ operator to allow us
    # using del my_array[key]
    def __delitem__(self, key: str) -> None:
        h = self.get_hash(key)
        self.arr[h] = None