class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = {}
        def optimal(row, col):
            if row == n - 1:
                return grid[row][col]

            if (row, col) in memo:
                return memo[(row, col)]

            next_minimum = inf
            for next_row_col in range(n):
                if next_row_col != col:
                    next_minimum = min(next_minimum, optimal(row + 1, next_row_col))

            memo[(row, col)] = grid[row][col] + next_minimum
            return memo[(row, col)]
        
        answer = inf
        for col in range(n):
            answer = min(answer, optimal(0, col))
        
        return answer