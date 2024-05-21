class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(ind, temp):
            if ind == len(s):
                ans.append(temp)
                return
            if s[ind].isdigit():
                backtrack(ind+1, temp + s[ind])
            else:
                backtrack(ind+1, temp + s[ind].lower())
                backtrack(ind+1, temp + s[ind].upper())
        
        backtrack(0, "")
        return ans