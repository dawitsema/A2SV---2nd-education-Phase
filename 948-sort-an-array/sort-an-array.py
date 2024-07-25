class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, left, right):
            if left == right:
                return [arr[left]]

            midd = (left + right) // 2
            leftPart = mergeSort(arr, left, midd)
            rightPart = mergeSort(arr, midd + 1, right)

            return merge(leftPart, rightPart)

        def merge(leftHalf, rightHalf):
            left = right = 0
            result = []
            while left < len(leftHalf) and right < len(rightHalf):
                if leftHalf[left] < rightHalf[right]:
                    result.append(leftHalf[left])
                    left += 1
                else:
                    result.append(rightHalf[right])
                    right += 1

            result.extend(leftHalf[left:])
            result.extend(rightHalf[right:])

            return result

        return mergeSort(nums, 0, len(nums) - 1)
