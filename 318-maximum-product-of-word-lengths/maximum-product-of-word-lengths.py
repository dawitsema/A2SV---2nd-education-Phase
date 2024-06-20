class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordbit = []
        for i in range(len(words)):
            temp = 0
            for ch in words[i]:
                pos = ord(ch) - 97
                temp |= (1 << pos)
            
            wordbit.append((temp, len(words[i])))
        
        maxx = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not wordbit[i][0] & wordbit[j][0]:
                    maxx = max(maxx, wordbit[i][1] * wordbit[j][1])
            
        return maxx
