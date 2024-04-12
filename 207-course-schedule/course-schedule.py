class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        color = [0] * numCourses
        
        def hasCycle(node):
            if color[node] == 1:
                return True
            if color[node] == 2:
                return False
            
            color[node] = 1
            for neighbor in graph[node]:
                if hasCycle(neighbor):
                    return True
            color[node] = 2
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True