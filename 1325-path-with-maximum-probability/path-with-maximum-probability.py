class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            val = succProb[i]
            graph[a].append([b, val])
            graph[b].append([a, val])

        suc = {node: float("-inf") for node in range(n)}
        suc[start_node] = 1
        processed = set()

        heap = [[-1, start_node]]
        while heap:
            prob, node = heapq.heappop(heap)
            prob = - prob
            if node in processed:
                continue
            processed.add(node)
            for child, val in graph[node]:
                tempProb = val * prob
                if tempProb > suc[child]:
                    suc[child] = tempProb
                    heapq.heappush(heap, [-tempProb, child])
        
        return suc[end_node] if suc[end_node] != float("-inf") else 0
