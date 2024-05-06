# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            temp = curr.val
            while stack and stack[-1] < temp:
                stack.pop()
            stack.append(temp)
            curr = curr.next
        
        if not stack:
            return None
        
        new_head = ListNode(stack[0])
        current = new_head
        for num in stack[1:]:
            current.next = ListNode(num)
            current = current.next
        
        return new_head