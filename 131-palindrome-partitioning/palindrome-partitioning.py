class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]  

        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]: 
                    for partition in dp[j]:
                        dp[i].append(partition + [s[j:i]])

        return dp[n]
