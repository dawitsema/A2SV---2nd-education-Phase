class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(row, col):
            if grid[row][col] == 0 or visited[row][col]:
                return 0
            visited[row][col] = True
            val = 1
            for r, c in direction:
                nr = r + row
                nc = c + col
                if inbound(nr, nc) and not visited[nr][nc]:
                    val += dfs(nr, nc)
            return val

        maxx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    maxx = max(maxx, dfs(i, j))

        return maxx
