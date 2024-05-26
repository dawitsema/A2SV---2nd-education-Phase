class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon) - 1, len(dungeon[0]) - 1
        memo = {}
        def dp(row, col):
            if row == m and col == n:
                return max(0, 0 - dungeon[row][col])
            if row > m or col > n:
                return float("inf")

            if (row, col) not in memo:
                memo[(row, col)] = max(min(dp(row+1,col), dp(row,col+1)) - dungeon[row][col], 0)

            return memo[(row, col)]
        return dp(0, 0) + 1
