class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:


        @cache
        def dp(state, tsum):
            for num in range(1, maxChoosableInteger + 1):
                if state >> num & 1:
                    continue
                if tsum + num >= desiredTotal or \
                not dp(state | 1 << num, tsum + num):
                    return True
            
            return False
        
        temp = (maxChoosableInteger + 1) * maxChoosableInteger//2
        if temp < desiredTotal:
            return False
        return dp(0, 0)


        