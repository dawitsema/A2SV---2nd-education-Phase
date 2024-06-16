class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missed = 1
        patches = 0
        i = 0

        while missed <= n:
            if i < len(nums) and missed >= nums[i]:
                missed += nums[i]
                i += 1
            else:
                missed *= 2
                patches += 1
        
        return patches
        