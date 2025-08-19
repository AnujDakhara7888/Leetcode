"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:   # <-- handles empty graph
            return None
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            copy = Node(node.val)
            clone[node]=copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy

        return dfs(node)


        
        