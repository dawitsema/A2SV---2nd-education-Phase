class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                temp = 1
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        temp = max(temp, 1 + dp(j))
                memo[i] = temp
            
            return memo[i]
        ans = 0
        for i in range(len(nums)):
            if i not in memo:
                ans = max(ans, dp(i))

        return ans