class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ticket = [ -1 for i in range(365)]
        for day in days:
            ticket[day - 1] = 1
        
        memo = {}
        def dp(i):
            while i < 365:
                if ticket[i]== 1:
                    break
                i += 1
            
            if i >= 365:
                return 0
            if i not in memo:
                memo[i] = min(dp(i+1) + costs[0], dp(i + 7) + costs[1], dp(i+30) + costs[2])
            return memo[i]

        return dp(0)

        



