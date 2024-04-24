class Solution:
    def __init__(self):
        self.nums = [0, 1, 1]
        for i in range(35):
            self.nums.append(self.nums[-1] + self.nums[-2] + self.nums[-3])

    def tribonacci(self, n: int) -> int:
        return self.nums[n]