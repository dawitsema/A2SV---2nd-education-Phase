class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tempSum = sum(rolls)
        currSum = mean * (n + len(rolls)) - tempSum
        if currSum > 6 * n or currSum < n:
            return []
        avg = currSum // n
        rem = currSum % n
        ans = [avg] * n
        for i in range(rem):
            ans[i] += 1
        return ans