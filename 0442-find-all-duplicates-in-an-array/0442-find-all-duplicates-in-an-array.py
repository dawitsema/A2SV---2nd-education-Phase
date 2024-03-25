class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        pt = 0
        while pt < len(nums):
            temp = nums[pt] - 1
            if temp != pt:
                if nums[temp] == nums[pt]:
                    pt +=1
                else:   
                    nums[temp], nums[pt] = nums[pt], nums[temp]
            else:
                pt += 1
        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(nums[i])
        
        return ans