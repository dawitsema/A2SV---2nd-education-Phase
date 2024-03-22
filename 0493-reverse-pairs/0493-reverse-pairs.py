class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(arr, left, right):
            if left >= right:
                return [arr[left]]
            midd = (left + right)//2
            leftHalf = mergeSort(arr, left, midd)
            rightHalf = mergeSort(arr, midd + 1, right)
            
            return merge(leftHalf, rightHalf)
        
        count = 0
        def merge(arr1, arr2):
            nonlocal count
            
            pt1 = 0
            pt2 = 0
            while pt1 < len(arr1) and pt2 < len(arr2):
                if arr1[pt1] > arr2[pt2] * 2 :
                    count += len(arr1) - pt1
                    pt2 += 1
                else:
                    pt1 += 1
                
            pt1 = 0
            pt2 = 0
            arr = []
            while pt1 < len(arr1) and pt2 < len(arr2):
                if arr1[pt1] < arr2[pt2]:
                    arr.append(arr1[pt1])
                    pt1 += 1
                else:
                    arr.append(arr2[pt2])
                    pt2 += 1
            
            arr.extend(arr1[pt1:])
            arr.extend(arr2[pt2:])
            
            return arr
        
        mergeSort(nums, 0, len(nums)-1)
        
        return count
                
            
            

        