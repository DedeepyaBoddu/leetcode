# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head==None:
            return False

        set1 = set()
        tail = head

        while tail.next!=None:
            if tail in set1:
                return True
            else:
                set1.add(tail)
                tail = tail.next

        return False
        