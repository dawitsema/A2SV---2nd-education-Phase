class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            temp = 0
            for j in range(i, n):
                temp += nums[j]
                arr.append(temp)

        arr.sort()
        ans = 0
        for i in range(left - 1, right):
            ans += arr[i]
        
        return ans % (10**9 + 7)
