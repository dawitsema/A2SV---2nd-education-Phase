class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for row in grid:
            for i in range(len(row)):
                row[i] = - row[i]
            
            heapq.heapify(row)
        
        for i in range(m):
            temp = 0
            for j in range(n):
                temp = max(temp, - heapq.heappop(grid[j]))
            
            ans += temp
        

        return ans
        
        