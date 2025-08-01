class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ref1 = Counter(nums1)
        ref2 = Counter(nums2)


        ans = []
        for num in ref1:
            t = min(ref1[num], ref2[num])
            if t > 0:
                arr = [num] * t
                ans.extend(arr)
            
        
        return ans