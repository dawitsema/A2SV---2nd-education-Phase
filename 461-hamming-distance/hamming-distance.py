class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = x ^ y
        a = bin(cnt)[2:]
        return a.count('1')

        