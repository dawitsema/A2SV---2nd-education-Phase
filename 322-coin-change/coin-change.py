class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(rem):
            if rem < 0:
                return float("inf")
            if rem == 0:
                return 0
            

            if rem not in memo:
                min_coin = float("inf")
                for coin in coins:
                    if rem - coin >= 0:
                        min_coin = min(dp(rem - coin) + 1, min_coin)

                memo[rem] = min_coin
            
            return memo[rem]

        result = dp(amount)

        return result if result != float("inf") else - 1


        