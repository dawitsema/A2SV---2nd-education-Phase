from sortedcontainers import SortedList
class MedianFinder:
    def __init__(self):
        self.nums = SortedList()
        self.k = 0
        

    def addNum(self, num: int) -> None:
        self.nums.add(num)
        self.k += 1
        
        

    def findMedian(self) -> float:
        if self.k%2:
            ind = self.k//2
            ans = float(self.nums[ind])
        else:
            ind = self.k//2
            ans = float((self.nums[ind] + self.nums[ind-1])/2)

        return ans
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()