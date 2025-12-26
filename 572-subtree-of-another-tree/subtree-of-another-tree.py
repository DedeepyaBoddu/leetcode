# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if self.isSameTree(node,subRoot):
                    return True
                else: 
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return False
            
                
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val == q.val:
                left = self.isSameTree(p.left,q.left)
                right = self.isSameTree(p.right,q.right)
                return left and right
            else:
                return False
        elif p == q == None:
            return True
        else: 
            return False         
        