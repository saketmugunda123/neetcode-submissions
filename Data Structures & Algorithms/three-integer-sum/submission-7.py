class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        #Idea: You have a first, left and right pointers. First is fixed and
        #then left and right perform 2 sum on the remaining portion of the arr.


        #Sort the nums array. That way you can use pointers to solve

        nums.sort()
        answerList = []
        for first in range(0, len(nums)):

            #Skipping over duplicate "first" values
            if nums[first] == nums[first -1] and first > 0:
                continue

            left = first + 1
            right = len(nums) -1

            while left < right:
                currSum = nums[first] + nums[left] + nums[right]

                if currSum < 0:
                    left +=1
                elif currSum > 0:
                    right -=1
                else:
                    answerList.append([nums[first], nums[left], nums[right]])
                    #increment one of the pointers
                    left +=1

                    #make sure that pointer doesn't end up at duplicate val
                    while nums[left] == nums[left -1] and left < right:
                        left +=1
        
        return answerList
                    



        





