class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero, n_zero = 0, 0

        while n_zero < len(nums):
            if nums[n_zero] != 0 and nums[zero] == 0:
                nums[n_zero], nums[zero] = 0, nums[n_zero]
                n_zero += 1
                zero += 1
            elif nums[n_zero] == 0 and nums[zero] == 0:
                n_zero += 1
            else:
                n_zero += 1
                zero += 1
    



        