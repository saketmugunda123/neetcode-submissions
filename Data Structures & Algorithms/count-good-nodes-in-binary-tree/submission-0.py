# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #basically keep track of the greatest seen node in each path
        self.goodNodes = 0
        def dfs(root, greatestNode):
            if not root:
                return

            #Checking to see if the current node is valid 
            #Compare curr node against greastest seen on this path so far
            newGreatest = greatestNode
            if root.val >= greatestNode.val:
                self.goodNodes +=1
                newGreatest = root
            
            left = dfs(root.left, newGreatest)
            right = dfs(root.right, newGreatest)
            return
        dfs(root,root)
        return self.goodNodes

            
        