class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        memo = {}
        
        def minScore(i, j):
            if j <= i + 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            min_score = float('inf')
            for k in range(i + 1, j):
                score = values[i] * values[k] * values[j]
                total_score = score + minScore(i, k) + minScore(k, j)
                min_score = min(min_score, total_score)
            
            memo[(i, j)] = min_score
            return min_score
        
        return minScore(0, n - 1)

