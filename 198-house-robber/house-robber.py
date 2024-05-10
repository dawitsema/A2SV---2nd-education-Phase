class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        memo = {}

        def dp(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            
            if n not in memo:
                memo[n] = max(dp(n-1), nums[n] + dp(n-2))
            
            return memo[n]
        
        return dp(n)