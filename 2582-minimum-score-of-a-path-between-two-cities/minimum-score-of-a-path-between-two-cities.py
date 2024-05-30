
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        unions = UnionFind(n + 1)
        res = float('inf')

        roads.sort(key=lambda x: x[2])  
        for d, i, j in roads:
            unions.union(d, i)
            
        for d, i, j in roads:
            if unions.find(1) != unions.find(d) or unions.find(n) != unions.find(i):
                continue
            res = min(res, j)

        return res 