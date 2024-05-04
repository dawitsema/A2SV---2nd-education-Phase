class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = 2**maximumBit - 1
        for num in nums:
            ans = ans ^ num

        res = [ans]
        for i in range(len(nums)-1, 0, -1):
            res.append(res[-1] ^ nums[i])

        return res