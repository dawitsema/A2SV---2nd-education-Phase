from sortedcontainers import SortedList
import bisect

class MyCalendar:

    def __init__(self):
        self.nums = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        ind = self.nums.bisect_right([startTime, endTime])
        
        if (ind > 0 and self.nums[ind - 1][1] > startTime) or (ind < len(self.nums) and self.nums[ind][0] < endTime):
            return False

        self.nums.add([startTime, endTime])
        return True

# Usage example:
# obj = MyCalendar()
# print(obj.book(10, 20))  # Expected True
# print(obj.book(15, 25))  # Expected False due to overlap with previous booking
# print(obj.book(20, 30))  # Expected True as it does not overlap
