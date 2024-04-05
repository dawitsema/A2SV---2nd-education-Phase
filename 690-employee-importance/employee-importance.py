"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {e.id: e for e in employees}
        def dfs(empid):
            employee = graph[empid]
            return (employee.importance + sum(dfs(empid) \
            for empid in employee.subordinates))
        
        return dfs(id)