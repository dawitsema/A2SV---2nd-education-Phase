class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs():
            while queue:
                    node, color = queue.popleft()
                    for ng in graph[node]:
                        if ng not in visited:
                            visited[ng] = 1 - color
                            queue.append((ng, 1-color))
                        elif visited[ng] == color:
                            return False
            return True

        visited = {}
        temp = True
        for v in range(len(graph)):
            if v not in visited:
                queue = deque([(v, 0)])
                visited[v] = 0
                temp = temp and bfs()

                
                # while queue:
                #     node, color = queue.popleft()
                #     for ng in graph[node]:
                #         if ng not in visited:
                #             visited[ng] = 1 - color
                #             queue.append((ng, 1-color))
                #         elif visited[ng] == color:
                #             return False
                
        return temp