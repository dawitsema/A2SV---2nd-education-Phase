class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            current_num = nums[i]

            if current_num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(current_num, max_prod * current_num)
            min_prod = min(current_num, min_prod * current_num)

            result = max(result, max_prod)

        return result
