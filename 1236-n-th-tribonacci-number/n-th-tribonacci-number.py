class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        for i in range(35):
            nums.append(nums[-1] + nums[-2] + nums[-3])

        return nums[n]