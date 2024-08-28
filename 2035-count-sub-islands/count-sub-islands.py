class Solution:
    # Directions in which we can traverse inside the grids.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    def is_sub_island(self, x, y, grid1, grid2, visited):
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        is_sub_island = True

        pending_cells = deque()
        pending_cells.append((x, y))
        visited[x][y] = True

        # Traverse on all cells using the breadth-first search method.
        while pending_cells:
            curr_x, curr_y = pending_cells.popleft()

            if not self.is_cell_land(curr_x, curr_y, grid1):
                is_sub_island = False

            for direction in self.directions:
                next_x = curr_x + direction[0]
                next_y = curr_y + direction[1]
   
                if (
                    0 <= next_x < total_rows
                    and 0 <= next_y < total_cols
                    and not visited[next_x][next_y]
                    and self.is_cell_land(next_x, next_y, grid2)
                ):
                    pending_cells.append((next_x, next_y))
                    visited[next_x][next_y] = True
        return is_sub_island

    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        visited = [[False] * total_cols for _ in range(total_rows)]
        sub_island_counts = 0

        # Iterate on each cell in 'grid2'
        for x in range(total_rows):
            for y in range(total_cols):

                if (
                    not visited[x][y]
                    and self.is_cell_land(x, y, grid2)
                    and self.is_sub_island(x, y, grid1, grid2, visited)
                ):
                    sub_island_counts += 1

        return sub_island_counts