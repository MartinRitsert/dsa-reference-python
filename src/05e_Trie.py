from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie. O(m) time, O(1) space."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Check if an exact word exists in the trie. O(m) time, O(1) space."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with the given prefix. O(m) time, O(1) space."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word: str) -> bool:
        """Delete a word from the trie. O(m) time, O(m) space for recursion stack."""
        if not self.search(word):
            return False

        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            """Return True if parent should delete this node."""
            if depth == len(word):
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[depth]
            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete(self.root, word, 0)
        return True


if __name__ == "__main__":
    trie = Trie()

    # Insert words
    for word in ["apple", "app", "application", "banana", "band"]:
        trie.insert(word)

    # Search tests
    assert trie.search("apple"), "Should find 'apple'"
    assert trie.search("app"), "Should find 'app'"
    assert not trie.search("appl"), "Should not find incomplete word 'appl'"
    assert trie.search("banana"), "Should find 'banana'"
    assert not trie.search("ban"), "Should not find incomplete word 'ban'"
    assert not trie.search("cat"), "Should not find 'cat'"

    # Empty string tests
    trie.insert("")
    assert trie.search(""), "Should find empty string after insert"
    assert trie.starts_with(""), "Empty prefix should match"

    # Prefix tests
    assert trie.starts_with("app"), "Should find prefix 'app'"
    assert trie.starts_with("appl"), "Should find prefix 'appl'"
    assert trie.starts_with("ban"), "Should find prefix 'ban'"
    assert not trie.starts_with("cat"), "Should not find prefix 'cat'"

    # Delete tests
    trie2 = Trie()
    trie2.insert("apple")
    trie2.insert("app")

    assert trie2.delete("apple"), "Should delete 'apple'"
    assert not trie2.search("apple"), "'apple' should not exist after delete"
    assert trie2.search("app"), "'app' should still exist"

    assert not trie2.delete("banana"), "Should return False for non-existent word"
    assert trie2.delete("app"), "Should delete 'app'"
    assert not trie2.search("app"), "'app' should not exist after delete"

    print("All tests passed!")
