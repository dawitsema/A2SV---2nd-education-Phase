class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])

        queue = []
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = "#"

        for r, c in queue:
            for x, y in directions:
                nr = r + x
                nc = c + y

                if inbound(nr, nc) and mat[nr][nc] == "#":
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat

            