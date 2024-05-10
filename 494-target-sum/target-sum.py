class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, summ):
            if i == len(nums):
                if summ == target:
                    return 1
                else:
                    return 0

            if (i, summ) not in memo:
                memo[(i, summ)] = dp(i+1, summ - nums[i]) + dp(i+1, summ + nums[i])

            return memo[(i, summ)]
        print(memo)
        return dp(0, 0)
            

