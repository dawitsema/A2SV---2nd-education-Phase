class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min, global_max = arrays[0][0], arrays[0][-1]
        result = 0
        
        for arr in arrays[1:]:
            local_min, local_max = arr[0], arr[-1]
            
            result = max(result, max(local_max - global_min, global_max - local_min))
            
            global_min = min(global_min, local_min)
            global_max = max(global_max, local_max)
        
        return result