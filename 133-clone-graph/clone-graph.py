"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}

        def dfs(i):
            if not i:
                return None
            if i in hmap:
                return hmap[i]
            clone = Node(i.val)
            hmap[i] = clone
            clone.neighbors = [dfs(neighbor) for neighbor in i.neighbors]
            return clone
        return dfs(node)
        
        



        