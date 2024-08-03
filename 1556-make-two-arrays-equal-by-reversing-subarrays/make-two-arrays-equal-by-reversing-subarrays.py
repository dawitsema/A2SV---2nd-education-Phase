class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(arr) == Counter(target)