class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
                    
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaf = [i for i in range(n) if len(graph[i]) == 1]

        while n > 2:
            n -= len(leaf)
            new_leaf = []
            for l in leaf:
                node = graph[l].pop()
                graph[node].remove(l)
                
                if len(graph[node]) == 1:
                    new_leaf.append(node)

            leaf = new_leaf
        
        return leaf
        