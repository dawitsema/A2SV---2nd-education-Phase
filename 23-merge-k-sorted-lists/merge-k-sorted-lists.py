# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        pt = 0
        while pt < len(lists):
            curr = lists[pt]
            while curr:
                arr.append(curr.val)
                curr = curr.next
            pt += 1
        heapify(arr)
        head = ListNode()
        ans = head
        while arr:
            ans.next = ListNode(heappop(arr))
            ans = ans.next
        return head.next