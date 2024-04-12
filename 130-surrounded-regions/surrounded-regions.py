class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                if inbound(r,c) and board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        queue.append((r + dr, c + dc))
        
        for col in range(cols):
            if board[0][col] == "O":
                bfs(0, col)
            if board[rows-1][col] == "O":
                bfs(rows-1, col)

        for row in range(rows):
            if board[row][0] == "O":
                bfs(row, 0)
            if board[row][cols-1] == "O":
                bfs(row, cols-1)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
