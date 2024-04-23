class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graphs = defaultdict(list)
        indegree = [0]*len(graph)
        for i in range(len(graph)):
            for node in graph[i]:
                graphs[node].append(i)
                indegree[i] += 1
  
        queue = deque([i for i, x in enumerate(indegree) if x == 0])
        safe = [False]*len(graph)
        
        while queue:
            node = queue.popleft()
            safe[node] = True
            for ng in graphs[node]:
                indegree[ng] -= 1
                if indegree[ng] == 0:
                    queue.append(ng)
        safeNodes = [i for i in range(len(graph)) if safe[i]]

        return safeNodes