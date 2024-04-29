class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        def union(x, y):
            xval = find(x)
            yval = find(y)
            if xval != yval:
                if size[xval-1] > size[yval-1]:
                    parent[yval] = xval
                    size[xval-1] += size[yval-1]
                else:
                    parent[xval] = yval
                    size[yval-1] += size[xval-1]
        
        def conected(x, y):
            return find(x) == find(y)

        parent = {1:1}
        size = [1]*1000
        ans = []
        for a, b in edges:
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            
            if conected(a, b):
                ans.append([a, b])
            else:
                union(a, b)
        
        return ans[-1]


