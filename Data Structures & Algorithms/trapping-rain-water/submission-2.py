class Solution:
    def trap(self, height: List[int]) -> int:

        #Simply, at each index, the amount of water it can store is figured out by computing the max height from the left of the index and max height from the right of the index and subtracting whatever value is at your current index. Basically min(maxLeft,maxRight) is the max amount of water you can store at a speicfic index and you simply just subtract whatever bar is located there assuming it is less than maxLeft and maxRight

        #Now the good enoguh solution is simply determinign the maxLeft and maxRight at every index and then determinign the water at each index. However, this creates a solution of O(1) space.

        #There is a 2 pointer solution and I will write the code below and explain intuition below
        #The goal is to simply just know what maxLeft and maxRIght is at every index without storing it in an O(N) arr

        maxLeft = height[0]
        maxRight = height[len(height)-1]
        answer = 0
        left = 0
        right = len(height) -1

        while left < right:
            if maxLeft < maxRight:
                left +=1
                if min(maxLeft, maxRight) - height[left] > 0:
                    answer += min(maxLeft, maxRight) - height[left]
                maxLeft = max(maxLeft, height[left])
            else:
                right -=1
                if min(maxLeft, maxRight) - height[right] > 0:
                    answer += min(maxLeft, maxRight) - height[right]
                maxRight = max(maxRight, height[right])
        return answer





        