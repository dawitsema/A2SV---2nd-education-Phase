class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        point = 0
        n = len(t)

        for i in range(len(s)):
            if point < n and s[i] == t[point]:
                point += 1
        
        return len(t) - point if point < n else 0
        
        