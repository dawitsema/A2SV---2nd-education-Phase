class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        
        visited = set()
        temp = []

        def dfs(node):
            visited.add(node)
            for ng in graph[node]:
                if ng not in visited:
                    dfs(ng)
            temp.append(node)

        for i in range(n):
            if i not in visited:
                dfs(i)

        ans = [[] for _ in range(n)]
        for node in temp:
            for ng in graph[node]:
                ans[node].extend([ng] + ans[ng])
            ans[node] = list(sorted(set(ans[node])))
        
        return ans