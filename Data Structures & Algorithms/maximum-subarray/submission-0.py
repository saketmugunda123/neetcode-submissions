class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        #This is kadane's algorithim
        # There are two possible options at each subarray
        #   -1) Do you want to create a new subarray
        #   -2) Do you want to continue the existing subarray



        #Algorithim Explanation:
        # Starting at each index 1, you find the max between the the value at that index, and the 
        #subarray that contains both index 0 and 1. That max value becomes the new value at index 1.
        #Now, nums[1] contains the best case subarray up until that point. 
        #At index[2] you check if you want to continue adding to that subarr, or if you should start
        #a new subarray

        maxVal = nums[0]

        for i in range(1, len(nums)):

            #First compute the sum of the currSubArray (nums[i-1]) and current value
            newSum = nums[i -1] + nums[i]
            
            nums[i] = max(newSum, nums[i]) #choosing whether to append previous subarr or create new one

            maxVal = max(maxVal, nums[i])
        

        return maxVal

        