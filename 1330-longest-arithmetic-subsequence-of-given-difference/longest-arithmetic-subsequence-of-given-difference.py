class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        maxx = 0

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
            
            maxx = max(maxx, dp[num])
        
        return maxx