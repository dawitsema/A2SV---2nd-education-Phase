from sortedcontainers import SortedList

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if size[px] < size[py]:
                    parent[px] = py
                    size[py] += size[px]
                else:
                    parent[py] = px
                    size[px] += size[py]      

        def conected(x, y):
            return find(x) == find(y)


        distance = SortedList()     
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                temp = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j)
                distance.add(temp)


        parent = [i for i in range(len(points))]
        size = [1] * len(points)
        count = 0
        ans = 0
        for dist, x, y in distance:
            if not conected(x, y):
                count += 1
                ans += dist
                union(x, y)
            if count >= len(points):
                break
        
        return ans