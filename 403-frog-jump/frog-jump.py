class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dp(position, k):
            if position == stones[-1]:
                return True
            
            for jump in [k - 1, k, k + 1]:
                if jump > 0:
                    nextP = position + jump
                    if nextP in stones:
                        if dp(nextP, jump):
                            return True
            return False
        
        if stones[1] != 1:
            return False
            
        return dp(stones[1], 1)