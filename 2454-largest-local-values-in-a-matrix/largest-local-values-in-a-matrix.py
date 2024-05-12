class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(grid)-2):
            temp = []
            for j in range(len(grid)-2):
                val = max(grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
                temp.append(val)
            ans.append(temp)

        return ans

