class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # [10, 25, 64, 9, 4]
        # [25, 10, 8, 9 , 4]
        # [5 ,3, 8, 9, 4]
        gifts = [-gift for gift in gifts]

        heapq.heapify(gifts)
        while k:
            k -= 1

            curr = -heapq.heappop(gifts)

            fl  = floor(curr ** 0.5)
            heapq.heappush(gifts, -fl)

        answer = 0

        for g in gifts:
            answer += abs(g)
        return answer



        



    
        