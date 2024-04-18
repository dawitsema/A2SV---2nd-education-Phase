class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        perimeter = 0

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(grid, visited, row, col):
            nonlocal perimeter 
                    
            visited[row][col] = True
            for rb, cl in directions:
                new_row = row + rb
                new_col = col + cl

                if grid[row][col] == 1:
                    if not (inbound(new_row, new_col)) or grid[new_row][new_col] == 0:
                        perimeter += 1

                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col)

        dfs(grid, visited, 0, 0)

        return perimeter