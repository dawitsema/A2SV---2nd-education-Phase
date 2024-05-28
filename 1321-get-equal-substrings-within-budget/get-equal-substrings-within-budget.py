class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        
        count = 0
        summ = 0
        left = 0
        for right in range(len(costs)):
            summ += costs[right]
            while summ > maxCost:
                summ -= costs[left]
                left += 1
            count = max(count, right - left + 1)

        return count