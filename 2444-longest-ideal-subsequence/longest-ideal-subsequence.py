class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        letters = [0] * 26

        res = 0
        for i in range(N):
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(26):
                if abs(prev - curr) <= k:
                    best = max(best, letters[prev])

            letters[curr] = max(letters[curr], best + 1)
            res = max(res, letters[curr])
        return res