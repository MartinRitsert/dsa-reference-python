class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in the trie
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Prefix matching checks if the prefix is in the trie
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
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

    # Prefix tests
    assert trie.starts_with("app"), "Should find prefix 'app'"
    assert trie.starts_with("appl"), "Should find prefix 'appl'"
    assert trie.starts_with("ban"), "Should find prefix 'ban'"
    assert not trie.starts_with("cat"), "Should not find prefix 'cat'"

    print("All tests passed!")
