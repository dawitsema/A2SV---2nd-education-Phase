class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        nums = [i for i in range(1, n)]
        def dp(val):
            if val < 0:
                return 0
            if val == 0:
                return 1
            if val not in memo:
                ans = 0
                for num in nums:
                    ans = max(ans, dp(val - num)*num)
                memo[val] = ans
            
            return memo[val]
        
        return dp(n)

            