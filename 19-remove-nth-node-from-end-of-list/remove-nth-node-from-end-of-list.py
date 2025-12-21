# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        count = 0
        while ptr:
            count+=1
            ptr = ptr.next

        dummy = ListNode()
        dummy.next = head
        curr = dummy
        idx = count -n 
        i =0
    
        while curr:
            if i == idx:
                if n!=1:
                    tmp = curr.next.next
                    curr.next.next = None
                    curr.next = tmp
                else:
                    curr.next = None
                break
            else:
                i +=1
                curr = curr.next
        return dummy.next

























 