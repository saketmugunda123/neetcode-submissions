# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0
        def dfs(self, root):
            #base case
            if not root:
                return 0
            
            #iterate through neighbors
            left = dfs(self, root.left)
            right = dfs(self, root.right)
            
            #Making a chnage to maxPath
            self.maxPath = max(self.maxPath, left + right)

            #A node that sums left + right but left = maxDepth of left, not num nodes
            return max(left, right) + 1
        
        dfs(self, root)
        return self.maxPath

        




            
            


        