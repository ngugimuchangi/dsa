class TrieNode:
    def __init__(self, end=False) -> None:
        self.children = {}
        self.end = end


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        - Insert a word into the trie.
        - Args:
            word: The word to insert.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                # Sort the children by key to make it easier to print the words
                # in alphabetical order, otherwise use a list instead of a dict
                node.children = dict(sorted(node.children.items()))
            node = node.children[char]
        node.end = True

    def prefix(self, prefix: str) -> bool:
        """
        - Check if the prefix is in the trie.
        - Args:
            prefix: The prefix to check.
        - Returns True if the prefix is in the trie, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def search(self, word: str) -> bool:
        """
        - Check if the word is in the trie.
        - Args:
            word: The word to check.
        - Returns True if the word is in the trie, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def delete(self, word: str) -> bool:
        """
        - Delete a word from the trie.
        - Args:
            word: The word to delete.
        """
        def _delete(node: TrieNode, word: str, i: int) -> bool:
            if i == len(word):
                if not node.end:
                    return False
                node.end = False
                return True
            char = word[i]
            if char not in node.children:
                return False
            child = node.children[char]
            deleted = _delete(child, word, i + 1)
            if deleted and not node.children[char] and not node.end:
                del node.children[char]
            return deleted
        return _delete(self.root, word, 0)

    def print_words(self) -> None:
        """
        - Print all the words in the trie in alphabetical order.
        """
        def _print_words(node: TrieNode, word: str) -> None:
            if node.end:
                print(word)
            for char, child in node.children.items():
                _print_words(child, word + char)
        _print_words(self.root, "")


if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    trie.insert("app")
    trie.insert("search")
    trie.insert("trie")
    trie.insert("delete")
    trie.insert("cat")
    trie.insert("java")
    trie.insert("javascript")
    trie.insert("python")
    trie.print_words()
    print('_' * 50)
    print()
    print('"ap" is a prefix:', trie.prefix("ap"))
    print('"ap" is a word:', trie.search("ap"))
    print('_' * 50)
    print()
    print('delete "ap"', trie.delete("ap"))
    trie.print_words()
    print('delete "app"', trie.delete("app"))
    trie.print_words()
