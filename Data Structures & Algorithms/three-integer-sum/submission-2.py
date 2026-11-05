class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #First sort the array
        nums = sorted(nums)
        
#Now for each number in array, use two pointers on the rest of values
#Increment the left pointer if less than and right if greater than target
#Now change the starting value after the iteration
#Idea is that once you use -1, you have found all the possible values with negative 1

        answerList = []
        i = 0
        
        while i < len(nums) - 2:
            firstNum = nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                currSum = nums[left] + nums[right] + firstNum

                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    answerList.append([firstNum, nums[left], nums[right]])

                    # Skip duplicate values for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

            # Skip duplicate values for `i`
            while i < len(nums) - 2 and nums[i] == firstNum:
                i += 1

        return answerList
    
        