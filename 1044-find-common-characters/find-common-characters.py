class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ref = Counter(words[0])

        for word in words[1:]:
            temp = Counter(word)
            for ch in ref:
                ref[ch] = min(ref[ch], temp[ch]) 

        
        res = []
        for ch in words[0]:
            if ref[ch] > 0:
                res.append(ch)
                ref[ch] -= 1
        

        return res