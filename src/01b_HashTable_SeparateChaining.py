from __future__ import annotations

from typing import Any

# NOTE: For simplicity in this manual implementation, we assume keys are strings
# to demonstrate a basic hashing algorithm. In a real-world hash table (like Python's dict),
# keys can be any hashable type (using Python's built-in hash() function).


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        # Using lists for chains is the classic textbook approach. An alternative is to use
        # dicts for O(1) chain lookups, but that defeats the educational purpose since
        # Python's dict is itself a hash table. Lists also use less memory per bucket.
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
            if element[0] == key:
                self.arr[h][idx] = (key, val)
                return
        self.arr[h].append((key, val))

    def __getitem__(self, key: str) -> Any:
        """Retrieve value by key. O(k) avg, O(k + n) worst time, O(1) space."""
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        raise KeyError(key)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve value by key, returning default if missing. O(k) avg, O(k + n) worst time, O(1) space."""
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key: str) -> None:
        """Delete a key-value pair. O(k) avg, O(k + n) worst time, O(1) space."""
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return
        raise KeyError(key)


if __name__ == "__main__":
    ht = HashTable()

    # Basic operations
    ht["apple"] = 100
    ht["banana"] = 200
    ht["orange"] = 300

    assert ht["apple"] == 100, "Should retrieve apple"
    assert ht["banana"] == 200, "Should retrieve banana"
    assert ht["orange"] == 300, "Should retrieve orange"

    # Test KeyError for missing key
    try:
        _ = ht["grape"]
        assert False, "Should raise KeyError for non-existent key"
    except KeyError:
        pass  # Expected

    # Test get() method
    assert ht.get("grape") is None, "get() should return None for missing key"
    assert ht.get("grape", "default") == "default", "get() should return default value"
    assert ht.get("apple") == 100, "get() should return value for existing key"

    # Test update
    ht["apple"] = 150
    assert ht["apple"] == 150, "Should update apple"

    # Test delete
    del ht["banana"]
    try:
        _ = ht["banana"]
        assert False, "Should raise KeyError for deleted key"
    except KeyError:
        pass  # Expected

    # Test KeyError when deleting non-existent key
    try:
        del ht["nonexistent"]
        assert False, "Should raise KeyError when deleting non-existent key"
    except KeyError:
        pass  # Expected

    # Test collision handling (unlike NoCollisionHandling, this should work!)
    # "ab" and "ba" have same hash but separate chaining handles this
    ht["ab"] = "first"
    ht["ba"] = "second"
    assert ht["ab"] == "first", "Should retrieve 'ab' despite collision"
    assert ht["ba"] == "second", "Should retrieve 'ba' despite collision"

    # Test deleting one colliding key doesn't affect the other
    del ht["ab"]
    try:
        _ = ht["ab"]
        assert False, "Should raise KeyError for deleted 'ab'"
    except KeyError:
        pass  # Expected
    assert ht["ba"] == "second", "'ba' should still exist after deleting 'ab'"

    print("All tests passed!")
