# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None
        

        def merge(p,q):
            
            dummy = ListNode()
            tail = dummy

            while p and q:
                if p.val < q.val:
                    tail.next = p
                    tail = p
                    p = p.next
                else:
                    tail.next = q
                    tail = q
                    q = q.next

            tail.next = p or q

            return dummy.next



        j = 1
        

        while j < n:
            for i in range(0,n-j,j*2):
     
                lists[i] = merge(lists[i],lists[i+j])
            j *= 2


       

        return lists[0]

