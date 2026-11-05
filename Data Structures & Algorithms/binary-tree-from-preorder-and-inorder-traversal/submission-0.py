# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # base case is if preorder or inordern arrays don't exist (exist)
        if not preorder or not inorder:
            return
        
        #we basically iterate through the preorder array and then determine if its left or right
        #based on inorder array

        currNode = TreeNode(preorder[0])

        #finds value we are currently processing in the in order array
        mid = inorder.index(preorder[0])

        #Everything to the left of middle is in left subtree, everything right is in right subtree
        currNode.left = self.buildTree(preorder[1: mid + 1], inorder[0:mid])
        currNode.right = self.buildTree(preorder[mid + 1:], inorder[mid +1:])
        return currNode







        


        