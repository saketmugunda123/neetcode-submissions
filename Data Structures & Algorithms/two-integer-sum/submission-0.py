class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Basically everytime you run into a number in the arr,
        #you store its complement and the index of curr. Then, when we run into the 
        #complement, we simply return the curr index (complement) and the index of
        #the original value 


        complementDict = {}

        for i in range(0, len(nums)):
            if nums[i] in complementDict:
                return [complementDict[nums[i]], i]
            else:
                complementDict[target - nums[i]] = i
        

    
        