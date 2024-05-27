
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left, right = 1, n
        while left <= right:
            midd = (left + right)//2
            ind = n - bisect_left(nums, midd)
            if ind == midd:
                return midd
            elif ind < midd:
                right = midd - 1
            else:
                left = midd + 1

        return -1 

        