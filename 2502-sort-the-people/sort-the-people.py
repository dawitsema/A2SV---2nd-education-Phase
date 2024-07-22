class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = dict()
        hashmap = {heights[i]:names[i] for i in range(len(names))}
        
        heights = sorted(heights, reverse = True)
        ans = [hashmap[heights[i]] for i in range(len(heights))]

        return ans
        
        