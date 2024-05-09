class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}  

        def jump(n):
            if n == 1 or n == 0:
                return n
            if n not in memo:
                memo[n] = jump(n-1) + jump(n-2)
    
            return memo[n]

        return jump(1 + n)



        