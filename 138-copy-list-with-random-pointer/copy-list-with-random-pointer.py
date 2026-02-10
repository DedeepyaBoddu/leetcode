"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def DuplicateNode(node):
            if not node:
                return None
            if node in hmap:
                return hmap[node]
            else:
                temp = Node(node.val)
                hmap[node] = temp
                temp.next = DuplicateNode(node.next)
                temp.random = DuplicateNode(node.random)
            return temp

        hmap = {}

        return DuplicateNode(head)



        