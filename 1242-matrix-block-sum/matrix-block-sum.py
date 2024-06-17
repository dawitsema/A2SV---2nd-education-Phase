class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = sum(sum(mat[x][max(0, j-k):min(n, j+k+1)])
                                   for x in range(max(0, i-k), min(m, i+k+1)))
        return result