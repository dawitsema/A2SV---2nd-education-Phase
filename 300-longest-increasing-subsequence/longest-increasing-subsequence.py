class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        result = 0
        for num in nums:
            left_index, right_index = 0, result
            while left_index != right_index:
                middle_index = left_index + (right_index - left_index) // 2
                if tails[middle_index] < num:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index
            result = max(result, left_index + 1)
            tails[left_index] = num
        return result