from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:

        result = SortedList()
        count = 0

        for i, inst in enumerate(instructions):
            less = result.bisect_left(inst)
            great = i - result.bisect_right(inst)
            count += min(less, great)

            result.add(inst)

        return count % (10**9 + 7)
