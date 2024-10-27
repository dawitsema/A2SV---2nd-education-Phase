class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        summ = a + b + c
        if summ - max(a, b, c) >= max(a, b, c):
            return (a + b + c)//2
        
        return summ - max(a, b, c)
            
        