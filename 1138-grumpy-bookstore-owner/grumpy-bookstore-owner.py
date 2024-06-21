class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfied += customers[i]
        
        temp = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                temp += customers[i]
        maxx = temp
        for i in range(minutes, len(grumpy)):
            if grumpy[i-minutes] == 1:
                temp -= customers[i-minutes]
            if grumpy[i] == 1:
                temp += customers[i]
            maxx = max(temp, maxx)
        
        return maxx + satisfied


