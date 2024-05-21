class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(ind, currI):
            if ind == len(triangle):
                return 0
            if (ind, currI) not in memo:
                memo[(ind, currI)] = min(
                    dp(ind + 1, currI) + triangle[ind][currI],
                    dp(ind + 1, currI + 1) + triangle[ind][currI],
                )
            return memo[(ind, currI)]

        return dp(0, 0)
