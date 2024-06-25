class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)
        validF = 0

        count = 0
        for i in range(len(nums)):
            if i >= k:
                if flipped[i - k]:
                    validF -= 1

            if validF % 2 == nums[i]:
                if i + k > len(nums):
                    return -1

                validF += 1
                flipped[i] = True
                count += 1

        return count