class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
    
        suffixSum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i + 1]
        
        memo = {}
        def dp(i, M):
            if i >= n:
                return 0
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                if i + X <= n:
                    max_stones = max(max_stones, suffixSum[i] - dp(i + X, max(M, X)))
            
            memo[(i, M)] = max_stones
            return max_stones
        
        return dp(0, 1)
