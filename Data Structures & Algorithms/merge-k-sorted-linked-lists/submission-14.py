# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(p,q):
            
            dummy = ListNode()
            tail = dummy

            while p and q:
                if p.val < q.val:
                    tail.next = p
                    tail = tail.next
                    p = p.next
                else:
                    tail.next = q
                    tail = tail.next
                    q = q.next
            if p:
                tail.next = p
            if q:
                tail.next = q

            return dummy.next



        j = 1

        while j < len(lists):
            for i in range(0,len(lists),j*2):
                if i+j >= len(lists):
                    break
                lists[i] = merge(lists[i],lists[i+j])
            j *= 2


        if len(lists) == 0:
            return None

        return lists[0]

