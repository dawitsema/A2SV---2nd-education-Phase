class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent, depth):
            k = 1
            for ng in graph[node]:
                if ng != parent:
                    k += dfs(ng, node, depth + 1)      
            weights[node] += k
            depths[node] = depth
            return k

        def dfs2(node, parent, w):
            ans[node] = w
            for ng in graph[node]:
                if ng != parent:
                    dfs2(ng, node, w + n - 2*weights[ng])

        weights, depths, ans = [0]*n, [0]*n, [0]*n
        dfs(0,-1,0)
        dfs2(0,-1,sum(depths))
        return ans