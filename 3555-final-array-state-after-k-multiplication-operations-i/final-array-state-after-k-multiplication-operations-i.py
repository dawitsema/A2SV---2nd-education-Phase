class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, [nums[i], i])
        
        for i in range(k):
            temp = heapq.heappop(heap)
            num, ind = temp[0], temp[1]
            heapq.heappush(heap, [num * multiplier, ind])

        heap = sorted(heap, key=lambda x : x[1])
        print(heap)

        return [x[0] for x in heap]
        
        
        
        