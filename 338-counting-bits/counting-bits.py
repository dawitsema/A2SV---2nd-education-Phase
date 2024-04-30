class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]* (num + 1)
        for i in range(1, num + 1):
            if i % 2:
                ans[i] = (ans[i - 1] + 1)
            else:
                ans[i] = (ans[i // 2])
        return ans