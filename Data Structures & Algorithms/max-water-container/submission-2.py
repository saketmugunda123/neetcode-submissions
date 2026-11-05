class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #Imagine you have 2 winners poles (you will always get to them). The reaosn is you will eventually run into one of them. When you run into one of them (lets say its the right one), you can increment the winner or increment the left. Here is the thing, if you increment the winner, then that doesn't make any sense because that means the left is one greater than the winner with a greater width than the supposed other winner (so it is not the winner).

        left = 0
        right = len(heights) -1
        answer = 0
        while left < right:
            leftHeight = heights[left]
            rightHeight = heights[right]
            currArea = min(leftHeight, rightHeight)*(right - left)
            answer = max(answer, currArea)

            if leftHeight < rightHeight:
                left += 1
            else:
                right -=1
        
        return answer