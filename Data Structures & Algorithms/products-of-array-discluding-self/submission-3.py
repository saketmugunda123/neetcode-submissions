class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #create a prefix array that represents the multiplicative sum of every number before it
        #Do the same with a suffix array but now with every number that comes after it

        #Then simply multipl prefix[i]*suffix[i] as prefix[i] represents the we are effectively doing (every number before i)*(every number after i) which is product of everything except self

        prefix = [1]
        currSum = nums[0]
        for i in range(1, len(nums)):
            prefix.append(currSum)
            currSum *= nums[i]
        
        suffix = [1]
        currSum = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            suffix.append(currSum)
            currSum *= nums[i]
        
        suffix.reverse()

        answer = []
        for i in range(len(prefix)):
            answer.append(prefix[i]*suffix[i])
        
        return answer