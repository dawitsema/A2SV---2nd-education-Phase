class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x = sorted(score, reverse=True)
        rank = {}
        cnt = 0
        for i,n in enumerate(x):
            if i == 0:
                rank[n] = "Gold Medal"
            elif i == 1:
                rank[n] = "Silver Medal"
            elif i == 2:
                rank[n] = "Bronze Medal"
            else:
                rank[n] = str(i+1)
        
        ans = []
        for sc in score:
            ans.append(rank[sc])
        
        return ans
        

        