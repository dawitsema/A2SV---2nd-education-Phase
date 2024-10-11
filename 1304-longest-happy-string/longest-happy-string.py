import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        heap = []
        
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        while heap:
            cnt, ch = heapq.heappop(heap)
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                ans.append(ch2)
                if cnt2 + 1 < 0:
                    heapq.heappush(heap, (cnt2 + 1, ch2))
                heapq.heappush(heap, (cnt, ch))
            else:
                ans.append(ch)
                if cnt + 1 < 0:
                    heapq.heappush(heap, (cnt + 1, ch))
        
        return ''.join(ans)
