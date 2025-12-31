# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        if len(preorder)==0:
            return None

        
        root.val = preorder[0]    
        idx = inorder.index(preorder[0])

        l_po = preorder[1:idx+1] 
        l_io = inorder[0:idx]

        r_po = preorder[ (idx+ 1):]
        r_io = inorder[ (idx+1): ]


        root.left = self.buildTree(l_po, l_io)
        root.right = self.buildTree(r_po,r_io)
        return root


        