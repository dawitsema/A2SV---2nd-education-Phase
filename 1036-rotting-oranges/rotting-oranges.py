class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1


        time, fresh = 0, 0
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

                
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in direction:
                    nr = dr + r
                    nc = dc + c
                    if inbound(nr, nc):
                        fresh -= 1
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
            time += 1
        
        return time if fresh == 0 else -1

