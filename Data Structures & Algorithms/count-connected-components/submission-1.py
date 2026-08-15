from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:set() for i in range(n)}

        for n1,n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)

        seen = set()

        res = 0

        def bfs(i):
            q = deque([i])
            while q:
                cur = q.popleft()
                seen.add(cur)
                while adj[cur]:
                    neighbor = adj[cur].pop()
                    adj[neighbor].remove(cur)
                    q.append(neighbor)


        for i in range(n):
            if i in seen:
                continue
            res += 1
            bfs(i)

        return res

        

        