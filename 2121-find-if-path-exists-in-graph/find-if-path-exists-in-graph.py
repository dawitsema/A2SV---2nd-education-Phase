@cache
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        def dfs(node):
            if node == destination:
                return True
                
            visited.add(node)
            for ng in graph[node]:
                if ng not in visited:
                    found = dfs(ng)
                    if found:
                        return True
            return False

        return dfs(source)
                    
