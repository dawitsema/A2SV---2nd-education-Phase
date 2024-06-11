class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic1 = Counter(arr1)
        ans = []

        for i in range(len(arr2)):
            temp = [arr2[i]]*dic1[arr2[i]]
            ans.extend(temp)

        checker = set(ans)
        temp = []
        for n in arr1:
            if n not in checker:
                temp.append(n)
        temp = sorted(temp)
        ans = ans + temp
        
        return ans
        