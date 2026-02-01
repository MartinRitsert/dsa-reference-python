from typing import Optional, Any

# NOTE: For simplicity in this manual implementation, we assume keys are strings
# to demonstrate a basic hashing algorithm. In a real-world hash table (like Python's dict),
# keys can be any hashable type (using Python's built-in hash() function).

# IMPORTANT: Linear probing with deletion has a subtle issue. When an element is deleted,
# it leaves a None "hole" that can break retrieval of elements that were inserted after it
# due to collision. This implementation attempts to fix this by rehashing subsequent elements
# after deletion, but this adds complexity. An alternative approach is to use "tombstone"
# markers instead of None for deleted slots.


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

    def __setitem__(self, key: str, val: Any) -> None:
        """Insert or update a key-value pair. O(k) avg, O(k + n) worst time, O(1) space."""
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)

    def __getitem__(self, key: str) -> Optional[Any]:
        """Retrieve value by key. O(k) avg, O(k + n) worst time, O(1) space."""
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

    # # O(n) space and time - creates full list of MAX elements on every call
    # def get_prob_range(self, index: int) -> list[int]:
    #     """Return probe indices wrapping around the array. O(n) time and space."""
    #     # The * operator unpacks the elements of the range object and
    #     # the [] brackets create a new list containing these elements
    #     return [*range(index, len(self.arr))] + [*range(0, index)]

    # O(1) space - generator yields indices one at a time, allowing early exit
    def get_prob_range(self, index: int):
        """Yield probe indices wrapping around the array. O(n) time, O(1) space."""
        for i in range(index, self.MAX):
            yield i
        for i in range(0, index):
            yield i

    def find_slot(self, key: str, index: int) -> int:
        """Find next available slot via linear probing. O(1) avg, O(n) worst time, O(1) space."""
        prob_range = self.get_prob_range(index)

        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index

        raise OverflowError("Hashmap full")

    def __delitem__(self, key: str) -> None:
        """Delete a key and rehash subsequent probed entries. O(k) avg, O(nk) worst time, O(1) space."""
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)

        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                raise KeyError(key)

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

    # Test collision handling with linear probing
    # "ab" and "ba" have same hash but linear probing handles this
    ht["ab"] = "first"
    ht["ba"] = "second"
    assert ht["ab"] == "first", "Should retrieve 'ab' despite collision"
    assert ht["ba"] == "second", "Should retrieve 'ba' despite collision"

    # Test deleting one colliding key doesn't affect the other
    # (This tests the rehashing logic in __delitem__)
    del ht["ab"]
    assert ht["ab"] is None, "Deleted 'ab' should return None"
    assert ht["ba"] == "second", "'ba' should still exist after deleting 'ab'"

    # Test KeyError on deleting non-existent key
    try:
        del ht["nonexistent"]
        assert False, "Should raise KeyError for non-existent key"
    except KeyError:
        pass  # Expected

    print("All tests passed!")
