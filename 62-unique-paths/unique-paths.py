class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def help(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i > m - 1 or j > n - 1:
                return 0
            
            if (i, j) not in memo:
                memo[(i, j)] = help(i+1, j) + help(i, j+1)
            
            return memo[(i, j)]
            
        return help(0, 0)