class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1
        index = left
        while left <= right:
            mid = (left + right)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                index = mid
                left = mid + 1
            

        

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right)//2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] > target:
                right = mid - 1
            else:
                left = mid + 1


        return False