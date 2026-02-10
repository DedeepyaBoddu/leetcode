# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ptr = head
        count = 0
        while ptr:
            count +=1
            ptr = ptr.next
        
        idx = count - n
        i = 1

        if idx == 0:
            dummy.next = head.next
            return dummy.next

        ptr2 = dummy.next
        while i<idx:
            i +=1
            ptr2 = ptr2.next
        
        rem = ptr2.next.next
        ptr2.next.next = None
        ptr2.next = rem

        return dummy.next







        