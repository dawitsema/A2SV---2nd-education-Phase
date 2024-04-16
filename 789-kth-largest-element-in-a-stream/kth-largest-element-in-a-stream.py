class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = sorted(nums, reverse = True)[:k]
        self.c = k
        heapify(self.kth)
        
    def add(self, val: int) -> int:
        if len(self.kth) < self.c:
            heappush(self.kth, val)
        elif val > self.kth[0]:
            heappop(self.kth)
            heappush(self.kth, val)
            
        return self.kth[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)