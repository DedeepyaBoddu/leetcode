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
        if not head:
            return None
        curr = head
        #Interleave duplicate node after each node
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        
        #Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # remove interleaved nodes
        dummy = Node(0)
        curr_copy = dummy
        curr = head

        while curr:
            copy = curr.next
            curr_copy.next = copy
            curr.next = copy.next
            curr_copy = copy
            curr = curr.next
        
        return dummy.next
            

        


            