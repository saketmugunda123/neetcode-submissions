# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        from collections import deque
        q = deque()

        if not root:
            return []
 
        q.append(root)

        answerList = []
        while q:
            
            #append to level list
            level = []

            #Iterate over len(q) to get all the values in that level
            for i in range(0, len(q)): 
                currNode = q.popleft() #pop current node
                level.append(currNode.val) #add to the current level array

                #add currNode's children to q (these don't get iterated over bc we are itearing over
                # the original length of the queue)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        
            answerList.append(level)
        
        return answerList






       




      


