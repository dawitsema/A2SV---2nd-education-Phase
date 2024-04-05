class Solution:
    def maxPower(self, s: str) -> int:
        maxx = 0
        left = right = 0
        while right < len(s):
            if s[left] == s[right]:
                maxx = max(right - left + 1, maxx)
            else:
                left = right
            right += 1
        
        return maxx