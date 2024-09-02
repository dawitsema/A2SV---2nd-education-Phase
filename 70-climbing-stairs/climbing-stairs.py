class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def dp(n):
            if n in (1, 2):
                return n
            if n not in memo:
                memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]
        
        return dp(n)