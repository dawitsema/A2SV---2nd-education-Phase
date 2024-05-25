class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        temp, size = 0, 0
        left = 0
        found = False
        for right in range(len(nums)):
            temp += nums[right]
            while left <= right and temp > target:
                temp -= nums[left]
                left += 1
            if temp == target:
                found = True
                size = max(size, right - left + 1)

        return len(nums) - size if found else -1
        