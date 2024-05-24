class TrieNode:
    def __init__ (self):
        self.is_end = False
        self.children = [None for i in range(26)]

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
        
        current.is_end = True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        splited = sentence.split()
        ans = []
        for word in splited:
            current = trie.root
            temp = []
            flag = True
            for ch in word:
                ind = ord(ch) - 97
                temp.append(ch)
                if current.children[ind] and flag:
                    if current.children[ind].is_end:
                        break
                    current = current.children[ind]
                else:
                    flag = False
            
            temp = "".join(temp)
            ans.append(temp)
        
        return " ".join(ans)
                
                
            
        