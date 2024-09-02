class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

        if summ %2: return False

        half = summ // 2

        memo = {}

        def dp(idx , totsum):

            if totsum == 0:
                return True
            if idx >= len(nums) :
                return False

            if (idx , totsum) not in memo:
                memo[(idx , totsum )] = dp(idx + 1 , totsum - nums[idx]) or dp(idx + 1 , totsum)


            return memo[idx , totsum]


        return dp(0 , half)
