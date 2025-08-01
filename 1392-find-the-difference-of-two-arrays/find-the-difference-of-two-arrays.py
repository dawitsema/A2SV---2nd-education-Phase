class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        bothEl = set(set(nums1) & set(nums2))
        
        ans1 = []
        for num in set(nums1):
            if num not in bothEl:
                ans1.append(num)
        
        ans2 = []
        for num in set(nums2):
            if num not in bothEl:
                ans2.append(num)
            
        
        return [ans1, ans2]