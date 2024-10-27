class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.hashMap = set()
        for i in range(1, 1001):
            heapq.heappush(self.heap, i)
            self.hashMap.add(i)
        

    def popSmallest(self) -> int:
        poped = heapq.heappop(self.heap)
        self.hashMap.remove(poped)

        return poped

        
        

    def addBack(self, num: int) -> None:
        if num not in self.hashMap:
            heapq.heappush(self.heap, num)
            self.hashMap.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)