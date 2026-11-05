# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #every time you return, you are returning the depth at that given node

        if not root:
            return 0

        left = self.maxDepth(root.left) #Depth of left subtree
        right = self.maxDepth(root.right) #Depth of right subtree

        return max(left, right) + 1 #add plus 1 to count curr node



        