class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        result = []

        pac,atl = set(),set()

        def dfs(r,c,visited,preHeight):

            if r < 0 or c < 0 or r == m or c == n or (r,c) in visited or heights[r][c] < preHeight :
                return

            visited.add((r,c))

            dfs(r+1,c,visited,heights[r][c])     
            dfs(r-1,c,visited,heights[r][c])     
            dfs(r,c+1,visited,heights[r][c])    
            dfs(r,c-1,visited,heights[r][c])     

        for c in range(n):
            dfs(0,c,pac,heights[0][c])
            dfs(m-1,c,atl,heights[m-1][c])

        for r in range(m):
            dfs(r,0,pac,heights[r][0])
            dfs(r,n-1,atl,heights[r][n-1])  
        
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl :
                    result.append([r,c])

        return result            


        