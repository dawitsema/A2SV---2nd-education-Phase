class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0]*n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
            
        queue = deque([i for i, x in enumerate(indegree) if x == 0] )
        ans = [set() for _ in range(n)]
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for ng in graph[node]:

                    ans[ng].add(node)
                    for el in ans[node]:
                        ans[ng].add(el)
                    
                    indegree[ng] -= 1
                    if indegree[ng] == 0:
                        queue.append(ng)
        
        ans = [sorted(list(gr)) for gr in ans]
        return ans
        # visited = set()
        # temp = []

        # def dfs(node):
        #     visited.add(node)
        #     for ng in graph[node]:
        #         if ng not in visited:
        #             dfs(ng)
        #     temp.append(node)

        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)

        # ans = [[] for _ in range(n)]
        # for node in temp:
        #     for ng in graph[node]:
        #         ans[node].extend([ng] + ans[ng])
        #     ans[node] = list(sorted(set(ans[node])))
        
        # return ans
        