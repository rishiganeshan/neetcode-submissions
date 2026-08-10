# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 0, 1, 2, 3, 4, 5
        # want 3 steps
        # 0, 1, 2, 3, 4, 5, 6
        # want 4 steps


        slow, fast = head, head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
        
        # reverse list from slow
        prev = None
        cur = slow

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        l1, l2 = head, prev
        # l1 will be >= length of l2 by 1
        while l1:
            if l2:
                l1next = l1.next
                l2next = l2.next
                l1.next = l2
                l2.next = l1next
                l2 = l2next
                l1 = l1next
            else:
                l1.next = None
                l1 = l1.next


        

            

        