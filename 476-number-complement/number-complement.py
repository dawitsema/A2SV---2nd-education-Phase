class Solution:
    def findComplement(self, num: int) -> int:
        n = ''
        while num > 0:
            n += str(1 - num%2)
            num //= 2
  
        return int(n[::-1],2)
        