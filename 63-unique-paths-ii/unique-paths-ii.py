class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = defaultdict(int)
        def help(i, j):
            if i == m - 1 and j == n - 1 and obstacleGrid[i][j] == 0:
                return 1
            if i > m - 1 or j > n - 1:
                return 0
            
            if (i, j) not in memo and obstacleGrid[i][j] == 0:
                memo[(i, j)] = help(i+1, j) + help(i, j+1)
            
            return memo[(i, j)]
            
        return help(0, 0)