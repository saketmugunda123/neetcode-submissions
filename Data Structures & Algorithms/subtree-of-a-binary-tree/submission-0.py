# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False  # An empty tree cannot have a non-empty subtree
        
        if self.sameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtree
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q  # If either is None, both must be None to be equal
        
        if p.val != q.val:
            return False  # Values must be equal
        
        # Recursively compare left and right subtrees
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)