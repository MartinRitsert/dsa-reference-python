from typing import Optional, Any

# NOTE: For simplicity in this manual implementation, we assume keys are strings
# to demonstrate a basic hashing algorithm. In a real-world hash table (like Python's dict),
# keys can be any hashable type (using Python's built-in hash() function).


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key: str) -> int:
        """Compute hash index for a given key. O(k) time, O(1) space."""
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key: str, val: Any) -> None:
        """Insert or update a key-value pair. O(k) avg, O(k + n) worst time, O(1) space."""
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                return
        self.arr[h].append((key, val))

    def __getitem__(self, key: str) -> Optional[Any]:
        """Retrieve value by key. O(k) avg, O(k + n) worst time, O(1) space."""
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None

    def __delitem__(self, key: str) -> None:
        """Delete a key-value pair. O(k) avg, O(k + n) worst time, O(1) space."""
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return


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

    # Test collision handling (unlike NoCollisionHandling, this should work!)
    # "ab" and "ba" have same hash but separate chaining handles this
    ht["ab"] = "first"
    ht["ba"] = "second"
    assert ht["ab"] == "first", "Should retrieve 'ab' despite collision"
    assert ht["ba"] == "second", "Should retrieve 'ba' despite collision"

    # Test deleting one colliding key doesn't affect the other
    del ht["ab"]
    assert ht["ab"] is None, "Deleted 'ab' should return None"
    assert ht["ba"] == "second", "'ba' should still exist after deleting 'ab'"

    print("All tests passed!")
