# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        len_part = count // k
        remaining = count % k

        ans = []
        curr = head
        for i in range(k):
            ans.append(curr)
            part_size = len_part + (1 if remaining > 0 else 0)
            if curr:
                for _ in range(part_size - 1):
                    curr = curr.next
                remaining -= 1
                temp = curr.next
                curr.next = None
                curr = temp
        return ans
