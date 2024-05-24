class TrieNode():
    def __init__ (self):
        self.children = [None for i in range(2)]

class Trie():
    def __init__ (self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if not current.children[int(ch)]:
                current.children[int(ch)] = TrieNode()
            current = current.children[int(ch)]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie()
        binarynum = []
        for num in nums:
            bitrep = bin(num)[2:]
            if len(bitrep) < 32 :
                bitrep = "0" * (32 - len(bitrep)) + bitrep
            binarynum.append(bitrep)
        
        for bn in binarynum:
            trie.insert(bn  )

        maxx = 0
        ans = -1
        for nx in binarynum:
            result = ""
            
            current = trie.root
            for bit in nx:
                if bit == "0":
                    if current.children[1]:
                        result +="1"
                        current = current.children[1]
                    else:
                        result += "0"
                        current = current.children[0]
                else:
                    if current.children[0]:
                        result +="1"
                        current = current.children[0]
                    else:
                        result += "0"
                        current = current.children[1]
            ans = max(ans , int(result , 2))
        
        return ans 
        print(*binarynum)


        return 0

