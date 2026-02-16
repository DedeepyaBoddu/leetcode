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
        pre_l = preorder[1:idx+1]
        in_l = inorder[0:idx]
        pre_r = preorder[idx+1:]
        in_r = inorder[idx+1:]

        root.left = self.buildTree(pre_l, in_l)
        root.right = self.buildTree(pre_r, in_r)


        return root