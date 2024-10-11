class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])

        delay = {node: float("inf") for node in range(1, n + 1)}
        delay[k] = 0
        processed = set()

        heap = [[0, k]]
        while heap:
            time, node = heapq.heappop(heap)
            if node in processed:
                continue
            for child, val in graph[node]:
                new_time = time + val
                if new_time < delay[child]:
                    delay[child] = new_time
                    heapq.heappush(heap, [new_time, child])
        return max(delay.values()) if max(delay.values()) != float("inf") else -1