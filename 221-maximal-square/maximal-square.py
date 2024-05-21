class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dp(r, c):
            if r >= m or c >= n:
                return 0
            if (r, c) not in memo:
                right = dp(r, c+1)
                down = dp(r+1, c)
                both = dp(r+1, c+1)

                if matrix[r][c] == "1":
                    memo[(r, c)] = 1 + min(right, down, both)
                else:
                    memo[(r, c)] = 0
            
            return memo[(r, c)]
        
        dp(0, 0)
        side = max(memo.values())
        return side * side