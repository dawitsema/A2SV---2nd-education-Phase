import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, -1 * nums[i])
        
        for j in range(k):
            maxx = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -1 * ceil(maxx/3))
            score += maxx
        
        return score

        
        