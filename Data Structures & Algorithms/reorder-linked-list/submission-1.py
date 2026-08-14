# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
get l, r = head, head of 2nd half
r = head of reverse 2nd half
merge = merge l, r (starting withl)

[1,2,3,4,5][6,7,8,]

result
1,9,2,8,3,7,4,6

6,7,8,9


7,6,8,9
8,7,6,9
9,8,7,6

can't figure out better way doing same as before


"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        
        prev, cur, slow.next = None, slow.next, None

        while cur:
            nextNode = cur.next
            cur.next = prev
            prev,cur = cur,nextNode

        
        n1, n2 = head, prev

        while n2:
            toInsert = n2
            n2 = n2.next

            toInsert.next = n1.next
            n1.next = toInsert
            n1 = toInsert.next
        








        


        




        