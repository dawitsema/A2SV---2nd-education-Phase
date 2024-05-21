class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dp(ind, hold, count):
            if ind >= len(prices) or count == 2:
                return 0
            if (ind, hold, count) in memo:
                return memo[(ind, hold, count)]
            
            if hold:
                sell = dp(ind + 1, False, count + 1) + prices[ind]
                notsell = dp(ind + 1, True, count)
                memo[(ind, hold, count)] = max(sell, notsell)
            else:
                buy = dp(ind + 1, True, count) - prices[ind]
                skip = dp(ind + 1, False, count)
                memo[(ind, hold, count)] = max(buy, skip)
            
            return memo[(ind, hold, count)]
        
        return dp(0, False, 0)
