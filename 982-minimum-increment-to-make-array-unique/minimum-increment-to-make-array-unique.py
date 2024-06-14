class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                count += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        
        return count