class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        word = Counter(s1.split())
        ans = []
        for ch in s2.split():
            word[ch] += 1
        
        for ch in word:
            if word[ch] == 1:
                ans.append(ch)

        
        return ans
        