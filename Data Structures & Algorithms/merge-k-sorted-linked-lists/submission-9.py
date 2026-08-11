# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()

        def merge(p,q):
            if not lists[p] and lists[q]:
                return lists[q]
            if not lists[q] and lists[p]:
                return lists[p]
            if not lists[p] and not lists[q]:
                return p
                
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


        def expandl(node):
            res = []
            while node:
                res.append(node.val)
                node = node.next
            return res
        j = 1

        while j < len(lists):
            # print(j)
            for i in range(0,len(lists),j*2):
                if i+j >= len(lists):
                    break
                merge(i,i+j)
            j *= 2
            # print([expandl(l) for l in lists])
            # print()

        if len(lists) == 0:
            return None

        return lists[0]

