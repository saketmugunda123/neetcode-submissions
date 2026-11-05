class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Basically everytime you run into a number in the arr,
        #you store its complement and the index of curr. Then, when we run into the 
        #complement, we simply return the curr index (complement) and the index of
        #the original value 


        complementDict = {}
        for i in range(len(nums)):
            #already ran into complement
            if nums[i] in complementDict:
                return [complementDict[nums[i]],i ]
            complementDict[target - nums[i]] = i


    
        