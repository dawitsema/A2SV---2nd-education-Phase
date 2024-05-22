class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(val):
            if val == 0:
                return 1
            if val < 0:
                return 0
            
            if val not in memo:
                ans = 0
                for num in nums:
                    if val - num >= 0:
                        ans += dp(val - num)
                memo[val] = ans

            return memo[val]

        return dp(target)