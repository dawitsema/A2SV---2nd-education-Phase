class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for pr in prerequisites:
            graph[pr[1]].append(pr[0])
            indegree[pr[0]] += 1
        
        queue = deque([i for i, x in enumerate(indegree) if x == 0])
        ans = []
        count = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                count += 1
                ans.append(node)
                for ng in graph[node]:
                    indegree[ng] -= 1
                    if indegree[ng] == 0:
                        queue.append(ng)
            

        return ans if numCourses == count else []