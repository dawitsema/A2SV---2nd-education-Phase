class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort()
        
        ans, heap = [], []
        ind, time = 0, tasks[0][0]
        while ind < len(tasks) or heap:
            while ind < len(tasks) and tasks[ind][0] <= time:
                heappush(heap, [tasks[ind][1], tasks[ind][2]])
                ind += 1
            
            if heap:
                t, i = heappop(heap)
                ans.append(i)
                time += t
            else:
                time = tasks[ind][0]
        
        return ans