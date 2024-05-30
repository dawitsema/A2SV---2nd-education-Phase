class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        dictionary = defaultdict(list)
        for ind in range(N):
            dictionary[nums[ind]].append(ind)
        
        for key, value in dictionary.items():
            n = len(value)
            suffix_sum = sum(value)
            prefix_sum = 0
            for i in range(n):
                curr = dictionary[key][i]
                ans[curr] = (i * curr - prefix_sum) + (suffix_sum - curr - (n - 1 - i) * curr)
                suffix_sum -= curr
                prefix_sum += curr
    
        return ans