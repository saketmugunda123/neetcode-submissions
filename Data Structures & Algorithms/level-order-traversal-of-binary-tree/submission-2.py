# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque

        if not root:
            return []

        q = deque()        
        q.append(root)
        answer = []
        while q:
            currLevel = []
            for i in range(len(q)):
                curr = q.popleft()
                currLevel.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            answer.append(currLevel)
        return answer
                

