class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        temp = start ^ goal
        count = 0
        while temp:
            count += temp & 1  # Increment if the last bit is 1
            temp >>= 1 
        return count