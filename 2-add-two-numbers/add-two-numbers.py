# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2 or carry!=0:
            if not p1:
                zero_node = ListNode()
                p1 = zero_node
            if not p2:
                zero_node = ListNode()
                p2 = zero_node
            val = (carry + p1.val + p2.val) % 10
            carry = (carry + p1.val + p2.val) // 10
            node = ListNode(val)
            curr.next = node
            curr = curr.next
            p1 = p1.next
            p2 = p2.next
        
        return dummy.next

            
        