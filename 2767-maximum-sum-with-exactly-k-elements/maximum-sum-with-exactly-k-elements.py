class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        score = 0
        for _ in range(k):
            temp = -1*heapq.heappop(heap)
            score += temp
            heapq.heappush(heap, -(temp + 1))
        
        return score