class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        n = len(matrix[0])
        m = len(matrix)
        def dp(row, col):
            if row >= m:
                return 0
            if (row, col) not in memo:
                if col >= n-1:
                    memo[(row, col)] = min(dp(row + 1, col-1), dp(row + 1, col)) + matrix[row][col]
                elif col <= 0:
                    memo[(row, col)] = min(dp(row + 1, col), dp(row + 1, col+1)) + matrix[row][col]
                else:
                    memo[(row, col)] = min(dp(row + 1, col), dp(row + 1, col+1), dp(row+1, col-1)) + matrix[row][col]

            return memo[(row, col)]
        
        ans = float("inf")
        for i in range(n):
            ans = min(ans, dp(0, i))
        
        return ans