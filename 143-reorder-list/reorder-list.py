# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return 
            
        
        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        dummy= ListNode()
        dummy.next = slow.next
        slow.next = None
        #print("head",head)
        #print("next half", dummy.next)

        prev = None
        curr = dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #print("head",head)
        #print("next half reversed", prev)

        p1 = head
        p2 = prev

        while p1 and p2:
            n1 = p1.next
            n2 = p2.next

            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2
        
        return 
