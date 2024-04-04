class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        count = 0

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row, col):
            visited[row][col] = True
            for rw, cl in direction:
                nrw = rw + row
                ncl = cl + col

                if inbound(nrw, ncl) and not visited[nrw][ncl] and grid[nrw][ncl] == '1':
                    dfs(nrw, ncl)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    count += 1

        return count
