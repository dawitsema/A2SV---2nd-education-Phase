class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(arr):

            dp = [0] * (len(arr) + 2)

            for i in range(2, len(arr) + 2):
                dp[i] = max(dp[i-1], dp[i - 2] + arr[i-2])
            
            return max(dp)
        return max(solve(nums[1:]), solve(nums[:-1])) if len(nums) != 1  else nums[0]
    
