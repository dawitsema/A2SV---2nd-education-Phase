class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for u, v, w in edges:
            self.graph[u].append([v, w])
        

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])
        

    def shortestPath(self, node1: int, node2: int) -> int:
        distance  = {i: float("inf") for i in range(self.n)}
        distance[node1] = 0
        visited = set()

        heap = [[0, node1]]
        while heap:
            val, node = heapq.heappop(heap)
            if node in heap:
                continue
            
            visited.add(node)
            for v, w in self.graph[node]:
                if val + w < distance[v]:
                    distance[v] = val + w
                    heapq.heappush(heap, [val + w, v])

        if distance[node2] != float('inf'):
            return distance[node2]
        
        return -1


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)