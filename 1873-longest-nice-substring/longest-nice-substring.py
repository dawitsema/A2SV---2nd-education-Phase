class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(word):
            upp = set()
            low = set()
            for ch in word:
                if ch.isupper():
                    upp.add(ch)
                else:
                    low.add(ch)

            for ch in upp:
                if ch.lower() not in low:
                    return False
            
            for ch in low:
                if ch.upper() not in upp:
                    return False

            return True

        
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                sub = s[i:j]
                if helper(sub) and len(sub) > len(ans):
                    ans = sub
        
        return ans

        

