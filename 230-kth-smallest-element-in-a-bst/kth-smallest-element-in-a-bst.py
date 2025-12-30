# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list1 = []
        def recursion(node: Optional[TreeNode]):
            if not node:
                return
            recursion(node.left)
            list1.append(node.val)
            recursion(node.right)
        recursion(root)
        return list1[k-1]
        
                

        

        
        