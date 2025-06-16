class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minn = float("inf")
        ans = 0

        for num in nums:
            minn = min(minn, num)
            ans = max(num - minn, ans)

        
        return -1 if ans == 0 else ans
        