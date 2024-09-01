class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(m)]
        k = 0
        arrLen = len(original)

        for i in range(m):
            for j in range(n):
                if k < arrLen:
                    matrix[i][j] = original[k]
                    k += 1
                else:
                    return []
        
        if matrix[m-1][n-1] != 0 and k == arrLen:
            return matrix
        else:
            return []