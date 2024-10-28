from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.words = []  # Store words for suggestions at each node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for ch in word:
            indx = ord(ch) - ord('a')
            if not curr.children[indx]:
                curr.children[indx] = TrieNode()
            curr = curr.children[indx]
            if len(curr.words) < 3:  # Only keep top 3 lexicographical words
                curr.words.append(word)
        curr.is_end = True
    
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        curr = self.root
        for ch in prefix:
            indx = ord(ch) - ord('a')
            if not curr.children[indx]:
                return []
            curr = curr.children[indx]
        return curr.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        
        # Sort products lexicographically
        products.sort()
        
        # Insert each product into the Trie
        for word in products:
            trie.insert(word)
        
        # Collect suggestions for each prefix of searchWord
        ans = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            ans.append(trie.get_words_with_prefix(prefix))
        
        return ans
