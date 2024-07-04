class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, sm, prev = head.next, 0, head
        while cur:
            sm += cur.val
            if cur.val == 0:
                cur.val, sm = sm, 0
                prev.next = prev = cur
            cur = cur.next

        return head.next