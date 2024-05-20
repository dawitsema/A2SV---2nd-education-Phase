class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        temp = []
        def backtrack(ind):
            ans.append(temp.copy())
            for i in range(ind, len(nums)):
                temp.append(nums[i])
                backtrack(i+1)
                temp.pop()
        
        backtrack(0)
        result = 0
        for subset in ans:
            temp = 0
            for x in subset:
                temp ^= x
            result += temp

        return result


        