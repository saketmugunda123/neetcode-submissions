# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #You should be returning left and right (both subtrees need to be)

        #Define an interval at each node (like a range that value can fall into)


        def validBST(root, leftBound, rightBound):
            
            if not root:
                return True
            

            #if the value of the root does not fall into the interval, return false
            if root.val <= leftBound or root.val >= rightBound:
                return False


            #When going left, your rightBound changes (your max value is now this node)
            left = validBST(root.left, leftBound, root.val)
            
            #When going right, your leftBound changes (now your min value is this node)
            right = validBST(root.right, root.val, rightBound)

            return left and right

        return validBST(root, float('-inf'), float('inf'))





        