class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        second = 0
        i = 0
        while True:
            if k == i and tickets[i]  == 1:
                return second + 1
            elif tickets[i] != 0:
                second += 1
                tickets[i] -= 1
            
            i = (i+1)%len(tickets)

        return 0
            

        