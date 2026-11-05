# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #3 conditions
        #If the left subtree is equal, right subtree is equal, and curr val
        # is equal

        if not p and q: 
            return False
        
        if not q and p:
            return False
        
        if not p and not q:
            return True
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return (p.val == q.val) and left and right




        