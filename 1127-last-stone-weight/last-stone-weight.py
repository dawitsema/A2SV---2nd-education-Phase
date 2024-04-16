class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)

        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            if x != y:
                heappush(stones, x - y)
        
        return -stones[0] if len(stones) == 1 else 0

