class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = []
        for i in range(len(mat)):
            power.append([sum(mat[i]), i])
        
        heapq.heapify(power)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        
        return ans
        