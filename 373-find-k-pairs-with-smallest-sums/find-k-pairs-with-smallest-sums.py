import heapq
from typing import List, Tuple

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Edge case: if either of the lists is empty, return an empty list.
        if not nums1 or not nums2:
            return []
        
        minHeap = []
        # Initialize the heap with pairs from the first element in nums1 with all elements in nums2.
        for j in range(min(len(nums2), k)):
            heapq.heappush(minHeap, (nums1[0] + nums2[j], 0, j))
        
        ans = []
        while minHeap and len(ans) < k:
            curr_sum, i, j = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])
            
            # If the next element in nums1 is valid, push it to the heap.
            if i + 1 < len(nums1):
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return ans
