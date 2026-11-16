class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):               # O(L), L = len(word)
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word):               # O(L): whole word stored?
        node = self._find(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):        # O(L): any word with this prefix?
        return self._find(prefix) is not None

    def autocomplete(self, prefix):       # every stored word under the prefix
        results = []
        def collect(node, path):
            if node.is_word:
                results.append(path)
            for ch in sorted(node.children):
                collect(node.children[ch], path + ch)
        start = self._find(prefix)
        if start:
            collect(start, prefix)
        return results


trie = Trie()
for word in ("car", "cat", "cart", "do", "dog"):
    trie.insert(word)
print(trie.search("car"), trie.search("ca"))   # True False
print(trie.starts_with("ca"))                  # True
print(trie.autocomplete("ca"))                 # ['car', 'cart', 'cat']
