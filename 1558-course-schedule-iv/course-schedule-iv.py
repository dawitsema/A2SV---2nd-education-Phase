class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for pr in prerequisites:
            graph[pr[0]].append(pr[1])
            indegree[pr[1]] += 1

        queue = deque([i for i, x in enumerate(indegree) if x == 0] )
        ans = [[False]*n for _ in range(n)]

        while queue:
            node = queue.popleft()
            for ng in graph[node]:
                ans[ng][node] = True
                for i in range(n):
                    if ans[node][i]:
                        ans[ng][i] = True

                indegree[ng] -= 1
                if indegree[ng] == 0:
                    queue.append(ng)
        
        res = []
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            x = ans[b][a]
            res.append(x)
        
        return res
        
    