"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
oldToNew = {}
def dfs(node):
    if node in oldToNew:
        return
    oldToNew[node] = Node(node.val)
    for neighbor in node.neighbors:
        if neighbor not in oldToNew:
            dfs(neighbor)
        oldToNew[node].neighbor.append(oldToNew[neighbor])


"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(old):
            if not old:
                return
            if old in oldToNew:
                return
            oldToNew[old] = Node(old.val)
            for neighbor in old.neighbors:
                if neighbor not in oldToNew:
                    dfs(neighbor)
                oldToNew[old].neighbors.append(oldToNew[neighbor])
            return oldToNew[old]
        
        return dfs(node)

        