class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        visited = set()
        def dp(rem: int, ind: int) -> int:
            if rem == 0:
                return 1
            if rem < 0 or ind == len(coins):
                return 0
            if (rem, ind) not in memo:
                memo[(rem, ind)] = dp(rem, ind + 1) + dp(rem - coins[ind], ind)
            
            return memo[(rem, ind)]
        
        return dp(amount, 0)
