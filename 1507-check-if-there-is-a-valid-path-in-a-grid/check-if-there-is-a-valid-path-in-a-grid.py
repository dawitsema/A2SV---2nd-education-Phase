from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        direction = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        destination = (len(grid) - 1, len(grid[0]) - 1)

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set([(0, 0)])
        stack = [(0, 0)]

        while stack:
            row, col = stack.pop()

            if (row, col) == destination:
                return True

            for r, c in direction[grid[row][col]]:
                nr = row + r
                nc = col + c
                if inbound(nr, nc) and (nr, nc) not in visited and (-r, -c) in direction[grid[nr][nc]]:
                    visited.add((nr, nc))
                    stack.append((nr, nc))

            

        return False
