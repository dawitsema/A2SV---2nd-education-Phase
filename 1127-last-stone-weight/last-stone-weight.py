class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        # x = heapq.heappop(stones)
        # y = heapq.heappop(stones)
        # if x != y:
        #     heapq.heappush(stones, x - y)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        
        return -stones[0] if len(stones) == 1 else 0

