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
        """Compute hash index for a given key. O(k) time, O(1) space."""
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    # def add(self, key: str, val: Any) -> None:
    #     """Insert or update a key-value pair. O(k) time, O(1) space."""
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    # def get(self, key: str) -> Any:
    #     """Retrieve value by key. O(k) time, O(1) space."""
    #     h = self.get_hash(key)
    #     return self.arr[h]
    
    # To be able to use my_array[key] = value instead of my_array.add(key, value),
    # we can overwrite the __setitem__ operator
    def __setitem__(self, key: str, val: Any) -> None:
        """Insert or update a key-value pair. O(k) time, O(1) space."""
        h = self.get_hash(key)
        self.arr[h] = val

    # To be able to use my_array[key] instead of my_array.get(key),
    # we can overwrite the __getitem__ operator
    def __getitem__(self, key: str) -> Optional[Any]:
        """Retrieve value by key. O(k) time, O(1) space."""
        h = self.get_hash(key)
        return self.arr[h]
    
    # Can also overwrite the __delitem__ operator to allow us
    # using del my_array[key]
    def __delitem__(self, key: str) -> None:
        """Delete a key-value pair. O(k) time, O(1) space."""
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == "__main__":
    ht = HashTable()

    # Basic operations
    ht["apple"] = 100
    ht["banana"] = 200
    ht["orange"] = 300

    assert ht["apple"] == 100, "Should retrieve apple"
    assert ht["banana"] == 200, "Should retrieve banana"
    assert ht["orange"] == 300, "Should retrieve orange"
    assert ht["grape"] is None, "Non-existent key should return None"

    # Test update
    ht["apple"] = 150
    assert ht["apple"] == 150, "Should update apple"

    # Test delete
    del ht["banana"]
    assert ht["banana"] is None, "Deleted key should return None"

    # Demonstrate collision problem (WARNING: this is expected to fail!)
    # "ab" and "ba" have same hash (ord('a') + ord('b') = ord('b') + ord('a'))
    ht["ab"] = "first"
    ht["ba"] = "second"  # This overwrites "ab" due to collision!
    assert ht["ab"] == "second", "Collision: 'ab' was overwritten by 'ba'"

    print("All tests passed!")