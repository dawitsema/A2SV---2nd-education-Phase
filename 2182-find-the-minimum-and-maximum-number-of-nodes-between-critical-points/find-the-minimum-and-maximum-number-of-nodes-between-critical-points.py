# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp,lst=head.next,[]
        prev=head
        i=1
        count=0
        while temp.next:
            if (prev.val<temp.val and temp.val>temp.next.val) or (prev.val>temp.val and temp.val<temp.next.val):
                lst.append(i)
                count+=1
            i+=1
            temp=temp.next
            prev=prev.next
        if count<2:
            return [-1,-1]
        else:
            res=[]
            min1=lst[-1]
            for i in range(len(lst)-1):
                min1=min(min1,(lst[i+1]-lst[i]))
            res.append(min1)    
            res.append(lst[-1]-lst[0])
        return res     
        