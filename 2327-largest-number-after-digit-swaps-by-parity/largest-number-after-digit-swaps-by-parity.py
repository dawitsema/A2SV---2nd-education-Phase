class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        for ch in str(num):
            temp = int(ch) 
            if temp % 2 == 1:
                heapq.heappush(odd, -temp)
            else:
                heapq.heappush(even, -temp)

        ans = 0
        for ch in str(num):
            temp = int(ch)
            if temp % 2 == 1:
                ans *= 10
                ans += -heapq.heappop(odd)
            else:
                ans *= 10 
                ans += -heapq.heappop(even)
        
        return ans