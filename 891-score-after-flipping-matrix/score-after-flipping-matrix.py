class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        for j in range(n):
            count = 0
            for i in range(m):
                if grid[i][j]:
                    count += 1
            if ceil(m/2) > count:
                for k in range(m):
                    grid[k][j] = 1 - grid[k][j]

        score = 0
        for i in range(m):
            s = ""
            for j in range(n):
                s += str(grid[i][j])

            score += int(s, 2) 
        
        return score