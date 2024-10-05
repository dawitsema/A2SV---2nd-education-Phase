class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for x in gifts:
            heapq.heappush(heap, -x)

        for i in range(k):
            temp = -heapq.heappop(heap)
            heapq.heappush(heap, -floor(pow(temp, 0.5)))

        return -sum(heap)
            
        