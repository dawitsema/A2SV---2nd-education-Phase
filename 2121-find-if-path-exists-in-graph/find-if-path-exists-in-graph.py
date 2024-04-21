@cache
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for child in graph[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        
        return False
                
        
