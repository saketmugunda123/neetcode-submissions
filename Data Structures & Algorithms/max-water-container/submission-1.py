class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Start 2 pointers at opposite sides of the array
        #Find the area. Then increment the side that is at a lower height
        #continue until left and right meet

        left = 0
        right = len(heights) -1
        answer = 0
        while left < right:

            currLength = right - left
            currWidth = min(heights[left], heights[right])

            currArea = currLength * currWidth

            answer = max(answer, currArea)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        
        return answer




        