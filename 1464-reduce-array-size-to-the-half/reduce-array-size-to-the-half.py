class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        heap = []
        n = len(arr)
        for val in count.values():
            heapq.heappush(heap, -val)
        
        cnt = 0
        ans = 0
        while cnt < (n + 1)//2:
            temp = -heapq.heappop(heap)
            cnt += temp
            ans += 1
            
        return ans