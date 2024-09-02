class Solution:
    def climbStairs(self, n: int) -> int:

        levels = [0, 1, 2]

        for i in range(3, n + 1):
            levels.append(levels[-1] + levels[-2])

        return levels[n]