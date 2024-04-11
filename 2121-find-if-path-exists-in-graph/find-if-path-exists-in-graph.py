@cache
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for child in graph[node]:
                if child not in visited:
                    stack.append(child)
                    visited.add(child)
        
        return False
                
        
