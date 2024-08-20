class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

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