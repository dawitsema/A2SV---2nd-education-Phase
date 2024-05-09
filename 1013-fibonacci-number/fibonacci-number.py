class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def help(i):
            if i == 1:
                return 1
            elif i == 0:
                return 0
            if i not in memo:
                memo[i] = help(i-1) + help(i-2)
            return memo[i]
        
        return help(n)