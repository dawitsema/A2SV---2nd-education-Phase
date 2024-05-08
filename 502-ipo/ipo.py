class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap = []
        for i in range(len(profits)):
            cap.append((capital[i], profits[i]))
        
        cap.sort()
        heap = []
        ans = w
        pt = 0
        for i in range(k):
            while pt < len(cap) and w >= cap[pt][0]:
                heappush(heap, -cap[pt][1])
                pt += 1
            if heap:
                x = -heappop(heap)
                ans += x
                w += x
            else:
                return ans
        
        return ans
            
