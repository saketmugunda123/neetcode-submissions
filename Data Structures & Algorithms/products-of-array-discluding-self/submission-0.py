class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        #Get prefix array (multiplication of everything before curr index)
        prefix = [1]*len(nums)
        prefixCounter = 1
        for i in range(1, len(nums)):
            prefixCounter *= nums[i-1]
            prefix[i] = prefixCounter
        

        #Get the suffix array (multiplication of everything after curr)
        suffix = [1]*len(nums)
        suffixCounter = 1
        for i in range(1, len(nums)):
            suffixCounter *= nums[len(nums) - i]
            suffix[len(nums) -i -1] = suffixCounter

        print(suffix)
        

        answerArr = [0]*len(nums)
        for i in range(0, len(prefix)):
            answerArr[i] = prefix[i]*suffix[i]
        
        return answerArr




        

