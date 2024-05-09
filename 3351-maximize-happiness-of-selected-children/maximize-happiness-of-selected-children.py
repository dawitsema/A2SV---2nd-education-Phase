class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        totalHappiness = 0
        sad = 0
        for i in range(k):
            if happiness[i] - sad <= 0:
                break
            totalHappiness += happiness[i] - sad
            sad += 1
        
        return totalHappiness