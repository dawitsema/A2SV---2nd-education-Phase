class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2

        memo = {}
        def dp(i, val):
            if val == 0: return True 
            if val < 0 or i >= len(nums): return False 

            if (i, val) not in memo:
                memo[(i, val)] = dp(i+1, val-nums[i]) or dp(i+1, val)
            
            return memo[(i, val)]

        return dp(0, target)
        