class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, robbed):
            if i >= len(nums):
                return 0

            if (i, robbed) not in memo:
                if i == 0:
                    one = nums[i] + dp(i + 2, True)
                    two = dp(i + 1, False)
                    memo[(i, robbed)] = max(one, two)
                elif i == len(nums) - 1:
                    if robbed:
                        memo[(i, robbed)] = 0
                    else:
                        memo[(i, robbed)] = nums[i]
                else:
                    one = nums[i] + dp(i + 2, robbed)
                    two = dp(i + 1, robbed)
                    memo[(i, robbed)] = max(one, two)
            return memo[(i, robbed)]

        return dp(0, False)


        