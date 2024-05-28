class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        ans = float("inf")
        ind = 0
        y = len(nums)
        for i in range(len(nums)):
            if i + 1 != y:
                x = abs(prefix[i+1]//(i+1) - (prefix[y] - prefix[i+1])//(y - i - 1))
            else:
                x = prefix[i+1]//(i+1)
            if ans > x:
                ind = i
                ans = x
        
        return ind
            