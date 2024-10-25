class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])


        distances = {(i, j) : float("inf") for j in range(len(grid[0])) for i in range(len(grid))}
        distances[(0, 0)] = 0
        visited = set()

        heap = [[0, (0, 0)]]
        while heap:
            val, node = heapq.heappop(heap)
            row, col = node
            if node in visited:
                continue
            visited.add(node)
            for r, c in direction:
                nr = row + r
                nc = col + c
                if inbound(nr, nc):
                    dist = val + grid[nr][nc]
                    if dist < distances[(nr, nc)]:
                        distances[(nr, nc)] = dist
                        heapq.heappush(heap, [dist, (nr, nc)])

        return distances[(len(grid) - 1, len(grid[0]) - 1)]
