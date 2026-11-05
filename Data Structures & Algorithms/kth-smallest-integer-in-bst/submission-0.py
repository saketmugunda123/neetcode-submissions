# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        
        def kSmallest(root):

            if not root:
                return

            
            left = kSmallest(root.left)

            self.count +=1

            if self.count == k:
                return root.val
            
            right = kSmallest(root.right)


            if left:
                return left
            else:
                return right
        
        return kSmallest(root)


        