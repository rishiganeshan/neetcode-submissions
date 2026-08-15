from collections import defaultdict,deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n == 1:
            return True

        adjList = defaultdict(set)
        for n1,n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)
        
        if len(adjList) < n:
            return False
        
        q = deque()

        for node, neighbours in adjList.items():
            if len(neighbours) == 1:
                q.append(node)

        """
        4,2,3
        2,3,1
        3,1
        1,
        """


        while q:
            # if len(q) == 2 and q[1] in adjList[q[0]] and q[0] in adjList[q[1]]:
            #     return True


            n -= 1
            cur = q.popleft()

            # print(cur)
            # print(adjList)
            # if cur not in adjList:
            #     return False
            # if not adjList[cur]:
            #     return False
            if not adjList[cur]:
                break
            parent = adjList[cur].pop()
  

            # if cur not in adjList[parent]:
            #     return False
            adjList[parent].remove(cur)
            # del adjList[cur]

            if len(adjList[parent]) == 1:
                q.append(parent)
        
        return n == 0

        

        