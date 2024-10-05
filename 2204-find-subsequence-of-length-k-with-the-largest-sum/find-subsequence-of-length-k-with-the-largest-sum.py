class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, [- nums[i], i])
        
        for j in range(k):
            temp = heapq.heappop(heap)
            ans.append([-temp[0], temp[1]])
        
        ans = sorted(ans, key=lambda x: x[1])
        return [x[0] for x in ans]


        
        return ans