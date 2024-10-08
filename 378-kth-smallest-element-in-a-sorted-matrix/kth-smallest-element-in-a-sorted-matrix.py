class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        heaplen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if heaplen >= k:
                    temp = heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, max(temp, -matrix[i][j]))
                    
                else:
                    heapq.heappush(maxHeap, -matrix[i][j])
                    heaplen += 1
        
        return -heapq.heappop(maxHeap)
        