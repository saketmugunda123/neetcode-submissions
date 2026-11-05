class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1

        currAnswer = 0
        answer = 0
        while left < right:
            currAnswer = (right - left) * (min(heights[left], heights[right]))

            answer = max(answer, currAnswer)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1


        return answer