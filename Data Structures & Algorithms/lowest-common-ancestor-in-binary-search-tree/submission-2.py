# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #want to return nodes at every point

        if not root:
            return
        

        #If we run into any of these values, 
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #Case 1: We want if the node we are at is a parent node of both
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
        


       


        
