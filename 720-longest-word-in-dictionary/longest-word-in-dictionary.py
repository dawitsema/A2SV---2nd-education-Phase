class TrieNode:
    def __init__ (self):
        self.children = [None for i in range(26)]
        self.is_end = False
        self.count = 0


class Trie:
    def __init__ (self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            ind = ord(ch) - 97
            if not current.children[ind]:
                current.children[ind] = TrieNode()
            current = current.children[ind]
            current.count += 1
        
        current.is_end = True
    def search(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix[:-1]:
            ind = ord(ch) - 97
            if not current.children[ind] or current.children[ind].count < 2 or not current.children[ind].is_end:
                return False
            current = current.children[ind]
        
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)

        ans = []
        maxx = 0
        for word in words:
            if trie.search(word):
                if len(word) > maxx:
                    ans = [word]
                    maxx = len(word)
                elif len(word) == maxx:
                    ans.append(word)
        
        return sorted(ans)[0] if ans else ""

        return ""


        