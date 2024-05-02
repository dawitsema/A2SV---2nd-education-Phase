class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            temp = -nums[left]
            if temp == nums[right]:
                return nums[right]
            elif temp < nums[right]:
                right -= 1
            else:
                left += 1
            
        return -1