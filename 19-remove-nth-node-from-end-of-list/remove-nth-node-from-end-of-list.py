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
        i = 0
        curr = dummy

        while curr:
            if i == idx:
                rem = curr.next.next
                curr.next.next = None
                curr.next = rem
                break
            else:
                i +=1
                curr = curr.next
      
        return dummy.next







        