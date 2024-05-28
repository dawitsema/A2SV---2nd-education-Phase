class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        def union(x, y):
            xval = find(x)
            yval = find(y)
            if xval != yval:
                if size[xval] > size[yval]:
                    parent[yval] = xval
                    size[xval] += size[yval]
                else:
                    parent[xval] = yval
                    size[yval] += size[xval]
     

        visited = {(stones[0][0], stones[0][1]): 0}
        size = {i:1 for i in range(len(stones))}
        parent = {i:i for i in range(len(stones))}
        
        for i in range(1, len(stones)):
            a, b = stones[i]
            for key, val in visited.items():
                if key[0] == a or key[1] == b:
                    union(val, i)
            
            visited[(stones[i][0], stones[i][1])] = i

        count = 0
        for i in range(len(stones)):
            if find(i) != i:
                count +=1

        return count


