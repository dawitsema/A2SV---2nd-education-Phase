class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a = (a & mask) if a < 0 else a
        b = (b & mask) if b < 0 else b
        
        while b:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & mask
        
        if a & (1 << 31):
            return ~(a ^ mask)
        
        return a
