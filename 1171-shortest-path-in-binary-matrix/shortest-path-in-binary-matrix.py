class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        distance = 1
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return distance
                for r, c in directions:
                    nr = r + row
                    nc = c + col
                    if inbound(nr, nc) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            distance += 1
        
        return -1