# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(p,q):
            if not p and q:
                return q
            if not q and p:
                return p
            if not p and not q:
                return p
            
            dummy = ListNode()
            tail = dummy

            while p or q:
                if not p:
                    tail.next = q
                    break
                if not q:
                    tail.next = p
                    break

                if p.val < q.val:
                    tail.next = p
                    tail = tail.next
                    p = p.next
                else:
                    tail.next = q
                    tail = tail.next
                    q = q.next

            return dummy.next
# merge every i,i+1
# merge i, i+2
# merge i, i+4
# merge i, i+8
# merge i, i+j
# j goes from 1,2,4,8,... up to 
# j is equal to len(lists) // 2 (or len(lists)+1)
# [1,2,3,4,5,6,7]
# [x,_,x,_,x,_,x]result after j=1 round
# [x,_,_,_,x,_,_] j=2
# [x,_,_,_,_,_,_] j=4

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
                lists[i] = merge(lists[i],lists[i+j])
            j *= 2
            # print([expandl(l) for l in lists])
            # print()

        if len(lists) == 0:
            return None

        return lists[0]

