from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        result = SortedList()
        count = 0
        for i in range(len(nums1)):
            greater = result.bisect_right(nums1[i] - nums2[i] + diff)
            count += greater

            result.add(nums1[i] - nums2[i])
        
        return count