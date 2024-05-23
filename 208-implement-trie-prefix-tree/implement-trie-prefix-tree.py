class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            ind = ord(ch) - 97
            if not current.children[ind]:
                current.children[ind] = TrieNode()
            current = current.children[ind]
        current.is_end = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            ind = ord(ch) - 97
            if not current.children[ind]:
                return False
            current = current.children[ind]
        
        return True if current.is_end else False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            ind = ord(ch) - 97
            if not current.children[ind]:
                return False
            current = current.children[ind]
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)