class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        def dfs(boss: int) -> int:
            return inform_time[boss] + max((dfs(emp) for emp in subordinates[boss]), default=0)

        subordinates = defaultdict(set)

        for u, v in enumerate(manager):
            subordinates[v].add(u)

        return dfs(head_id)