class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = [1, num]
            else:
                dictionary[num][0] += 1

        kth = [(-x, y) for x, y in dictionary.values()]
        heapify(kth)
        ans = []
        while k > 0:
            ans.append(heappop(kth)[1])
            k -= 1

        return ans