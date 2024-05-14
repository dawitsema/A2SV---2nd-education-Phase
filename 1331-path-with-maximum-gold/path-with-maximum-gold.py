class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if not inbound(row, col):
                return 0

            current_gold = grid[row][col]
            grid[row][col] = 0

            max_gold = 0
            for r, c in direction:
                nr = row + r
                nc = col + c
                max_gold = max(max_gold, dfs(nr, nc))

            grid[row][col] = current_gold
            return current_gold + max_gold

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))
        
        return ans
