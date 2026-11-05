class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Kadane's Alg: At each step, determine the best subarray ending at that index

        

        #For multiplcation you run into issues when multiplying by negatives
        #To account for this, keep track of the max and min values at each index

        maxValue = nums[0]
        minValue = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            #if nums[i] < 0, then that means maxValue and minValue need to be flipped
            #because maxValue will be able to now multiply negative by negative to get positive
            if nums[i] < 0:
                maxValue, minValue = minValue, maxValue

            #This is the max value and min subarrays ending at index i.
            maxValue = max(nums[i]*maxValue, nums[i])
            minValue = min(nums[i]*minValue, nums[i])

            answer = max(answer, maxValue)
        
        return answer

