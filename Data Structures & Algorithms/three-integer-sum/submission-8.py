class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        #Idea: You have a first, left and right pointers. First is fixed and
        #then left and right perform 2 sum on the remaining portion of the arr.


        #Sort the nums array. That way you can use pointers to solve

        res = []
        nums.sort()

        #have a first pointer, and then use l and r pointers on remaining list to close in on 
        #triplets

        for first in range(0, len(nums)):
            #check if first pointer reaches duplicate value
            #for each iter, we find all possible combin for nums[first] that add to 0
            if first > 0 and nums[first] == nums[first -1]:
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
                    res.append([nums[first], nums[left], nums[right]])

                    #increment left or right to start at a new value
                    left +=1
                    while nums[left] == nums[left -1] and left < right:
                        left +=1
        
        return res

                    



        





