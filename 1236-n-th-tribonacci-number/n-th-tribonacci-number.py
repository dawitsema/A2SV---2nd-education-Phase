class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(x):
            if x == 1 or x == 2:
                return 1
            if x == 0:
                return 0
            if x not in memo:
                memo[x] = dp(x-1) + dp(x-2) + dp(x-3)
            
            return memo[x]
        
        return dp(n)
        