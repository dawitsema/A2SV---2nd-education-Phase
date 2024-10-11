class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrow = len(heights)
        ncol = len(heights[0])
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def inbound(row, col):
            return 0 <= row < nrow and 0 <= col < ncol
        
        distances = {(row, col): float("inf") for col in range(ncol) for row in range(nrow)}
        distances[(0, 0)] = 0
        processed = set()

        heap = [[0, (0, 0)]]
        while heap:
            val, grid = heapq.heappop(heap)
            if (grid[0], grid[1]) in processed:
                continue
            processed.add((grid[0], grid[1]))
            for row, col in direction:
                nr = grid[0] + row
                nc = grid[1] + col
                if not inbound(nr, nc):
                    continue
                temp_dist = abs(heights[grid[0]][grid[1]] - heights[nr][nc])
                if temp_dist < distances[(nr, nc)]:
                    distances[(nr, nc)] = max(temp_dist, val)
                    heapq.heappush(heap, [max(temp_dist, val), (nr, nc)])

        return distances[(nrow - 1, ncol - 1)]