# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #Case 1: left and right have p and q
        #This means that you return your current node all the way up

        #Case 2 q is a descendent of p (or vice versa)
        #This means that you return the upper value up the tree

        #Base case
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p,q)

        if left and right:
            return root
        elif left and not right:
            return left
        else:
            return right


        
