# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #You actually shouldn't need recursion for this
        #This should just be regular BFS
        from collections import deque

        q = deque()

        if not root:
            return []

        q.append(root)
        tempArr = []
        answerArr = [[root.val]]

        while len(q) != 0:

            curr = q.popleft()

            if curr.left:
                tempArr.append(curr.left)

            if curr.right:
                tempArr.append(curr.right)


            if len(q) == 0:
                if tempArr:
                    for node in tempArr:
                        q.append(node)
                
                    tempArr2 = []
                    for node in tempArr:
                        tempArr2.append(node.val)    
                    tempArr = []
                    answerArr.append(tempArr2)
                
        return answerArr


        