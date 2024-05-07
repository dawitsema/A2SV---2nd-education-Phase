# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(root):
            prev = None
            curr = root
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        head = reverse(head)
        curr = head
        carry = 0
        prev = None
        while curr:
            temp = curr.val * 2 + carry
            curr.val = temp%10
            carry = temp//10
            prev = curr
            curr = curr.next
        if carry != 0:
            newNode = ListNode(carry)
            prev.next = newNode
            prev = newNode

        return reverse(head)

        



