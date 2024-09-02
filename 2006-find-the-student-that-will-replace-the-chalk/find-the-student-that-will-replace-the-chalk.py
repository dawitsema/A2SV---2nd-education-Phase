class Solution:
    def chalkReplacer(self, chalks: List[int], k: int) -> int:
            
        chalk_remain = k % (sum(chalks))

        for i, chalk in enumerate(chalks):
            if chalk_remain - chalk >= 0:
                chalk_remain -= chalk
            else:
                return i
        
        return 0


