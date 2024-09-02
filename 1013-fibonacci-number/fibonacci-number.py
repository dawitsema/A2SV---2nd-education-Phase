class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def dp(num):
            if num == 1 or num == 0:
                return num
            else:
                return dp(num -1) + dp(num - 2)
        
        return dp(n)
        