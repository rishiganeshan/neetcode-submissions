# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        prev = None

        for _ in range(n-1):
            fast = fast.next
        
        while fast.next:
            if not prev:
                prev = head
            else:
                prev = prev.next
            slow = slow.next
            fast = fast.next

        if not slow.next and not prev:
            return None
        if slow.next and not prev:
            return slow.next
        prev.next = slow.next
        return head