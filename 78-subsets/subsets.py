class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def helper(start):
            ans.append(sub.copy())
            for i in range(start, len(nums)):
                sub.append(nums[i])
                helper(i+1)
                sub.pop()
            return ans

        return helper(0)
        