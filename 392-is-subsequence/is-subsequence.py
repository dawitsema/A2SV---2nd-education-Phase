class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt = 0
        for i in range(len(t)):
            if pt == len(s):
                return True
            if s[pt] == t[i]:
                pt += 1
                
        if pt == len(s):
            return True
        return False

