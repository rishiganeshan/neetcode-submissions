# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode()

        def merge(p,q):                
            dummy.next = None
            tail = dummy

            while lists[p] or lists[q]:
                if not lists[p]:
                    tail.next = lists[q]
                    break
                if not lists[q]:
                    tail.next = lists[p]
                    break

                if lists[p].val < lists[q].val:
                    tail.next = lists[p]
                    tail = tail.next
                    lists[p] = lists[p].next
                else:
                    tail.next = lists[q]
                    tail = tail.next
                    lists[q] = lists[q].next

            lists[p] = dummy.next
            lists[q] = None

        j = 1

        while j < len(lists):
            for i in range(0,len(lists),j*2):
                if i+j >= len(lists):
                    break
                merge(i,i+j)
            j *= 2

        return lists[0]

