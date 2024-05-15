class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(buy, i):
            if i >= len(prices):
                return 0
            if (buy, i) not in memo:
                if prices[i] - buy > 0:
                    memo[(buy, i)] = max(dp(float("inf"), i+2) + prices[i] - buy , dp(buy, i+1) )
                else:
                    buy = min(buy, prices[i])
                    memo[(buy, i)] = dp(buy, i+1)
            return memo[(buy, i)]
        
        return dp(float("inf"), 0)