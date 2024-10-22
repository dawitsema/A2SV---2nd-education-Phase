class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        j = 1
        rightMax = [0]*len(nums)
        maxx = 0
        for i in range(len(nums)-1, -1, -1):
            maxx = max(maxx, nums[i])
            rightMax[i] = maxx

        while j < len(nums):
            if nums[i] <= rightMax[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
            # print(i, j, ans)
        
        return ans

