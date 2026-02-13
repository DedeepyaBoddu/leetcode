# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth_dfs(node):
            if not node:
                return 0
            left = depth_dfs(node.left)
            right = depth_dfs(node.right)
            self.res = max(self.res, left+right)
            return (1+max(left,right))
        
        _ = depth_dfs(root)
        return self.res
        