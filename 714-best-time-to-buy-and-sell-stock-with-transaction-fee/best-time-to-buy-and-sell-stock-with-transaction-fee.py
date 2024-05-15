class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(buy, i):
            if i >= len(prices):
                return 0
            if (buy, i) not in memo:
                if prices[i] - (buy + fee) > 0:
                    memo[(buy, i)] = max(dp(float("inf"), i+1) +prices[i] - (buy + fee) , dp(buy, i+1) )
                else:
                    buy = min(buy, prices[i])
                    memo[(buy, i)] = dp(buy, i+1)
            return memo[(buy, i)]
        
        return dp(float("inf"), 0)
