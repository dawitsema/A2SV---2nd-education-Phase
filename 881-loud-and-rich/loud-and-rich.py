class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        indegree = [0]*len(quiet)
        graph = defaultdict(list)
        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1
  
        quiet = [[x, i] for i, x in enumerate(quiet)]

        queue = deque([i for i, x in enumerate(indegree) if x == 0])
        ans = [0]*len(quiet)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[node] = quiet[node][1]

                for ng in graph[node]:
                    if quiet[ng][0] > quiet[node][0]:
                        quiet[ng][0] = quiet[node][0]
                        quiet[ng][1] = quiet[node][1]
                    indegree[ng] -= 1
                    if indegree[ng] == 0:
                        queue.append(ng)
        
        return ans

