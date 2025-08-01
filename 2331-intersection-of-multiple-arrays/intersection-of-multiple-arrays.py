class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        set1 = set(nums[0])
        
        for arr in nums[1:]:
            set1 = set1 & set(arr)
        
        return sorted(list(set1))