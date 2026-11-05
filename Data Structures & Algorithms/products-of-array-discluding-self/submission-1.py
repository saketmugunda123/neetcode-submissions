class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Get prefix array. This array stores the product before the value
        #shows up in the lsit

        prefix = [1]*len(nums)
        currTotPrefix = 1
        for i in range(len(nums)):
            prefix[i] = currTotPrefix
            currTotPrefix *= nums[i]
        

        #Get the suffix array. Stores product of values after nums[i]
        suffix = [1]*len(nums)
        currTotSuffix = 1
        for i in range(len(nums) -1, -1, -1):
            suffix[i] = currTotSuffix
            currTotSuffix *= nums[i]
        
        answerArr = []
        for i in range(0, len(nums)):
            answerArr.append(suffix[i]*prefix[i])
        
        return answerArr






        

