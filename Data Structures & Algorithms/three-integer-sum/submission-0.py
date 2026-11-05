class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #First sort the array
        nums = sorted(nums)
        
#Now for each number in array, use two pointers on the rest of values
#Increment the left pointer if less than and right if greater than target
#Now change the starting value after the iteration
#Idea is that once you use -1, you have found all the possible values with negative 1

        answerDict = {}
        for i in range(0, len(nums) -2):
            firstNum = nums[i]
            left = i + 1
            right = len(nums) -1

            while left < right:
                numLeft = nums[left]
                numRight = nums[right]
                currSum = numLeft + numRight + firstNum
                tempAnswer = None

                if currSum < 0:
                    left +=1
                elif currSum > 0:
                    right -=1
                else:
                    tempAnswer = (firstNum, numLeft, numRight)
                    left +=1
                    if tempAnswer not in answerDict:
                        answerDict[tempAnswer] = 1

                
                #Checking if the answer is a duplicate
                
        
        answerList = []
        for key in answerDict:
            tempKey = list(key)
            answerList.append(tempKey)
        
        return answerList
        
        