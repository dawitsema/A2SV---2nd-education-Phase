class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freqMap = Counter(nums)
        nextFreq = defaultdict(int)

        for num in nums:
            if freqMap[num] != 0:
                if nextFreq[num] != 0:
                    nextFreq[num] -= 1
                    nextFreq[num + 1] += 1
                elif freqMap[num + 1] > 0 and freqMap[num + 2] > 0:
                    freqMap[num + 1] -= 1
                    freqMap[num + 2] -= 1
                    nextFreq[num + 3] += 1
                else:
                    return False
                
                freqMap[num] -= 1
        return True
        