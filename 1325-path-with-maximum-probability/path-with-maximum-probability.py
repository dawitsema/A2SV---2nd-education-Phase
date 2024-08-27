from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (a, b), s in zip(edges, succProb):
            graph[a].append((b, s))
            graph[b].append((a, s))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        
        # Use a max-heap, with negative probability to simulate max behavior in heapq
        heap = [(-1.0, start_node)]
        
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob  # Convert back to positive
            
            if node == end_node:
                return prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))
        
        return 0.0  # If there's no path to the end_node
