class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        for i in range(0, len(nums), 2):
            temp1 = heapq.heappop(nums)
            temp2 = heapq.heappop(nums)
            ans.extend([temp2, temp1])
        
        return ans
        