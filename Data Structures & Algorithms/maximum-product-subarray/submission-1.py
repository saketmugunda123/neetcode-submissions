class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Kadane's Alg: At each step, determine the best subarray ending at that index

        #At each step, you want to keep track of the min and max at that particular step
        #Idea: know the min and max values up until that point

        #Instead of editing nums array directly, these keep track of nums[i-1] for us
        minValue = nums[0]
        maxValue = nums[0]
        answer = nums[0]

        #When nums[i] < 0, we swap maxValue and minValue. This is bc multiplying a negative
        #number by smaller value, yields a greater value. So you will get a better result
        #multiplying a negative number by the smaller of the two numbers
        for i in range(1, len(nums)):
            #Swapping values
            if nums[i] < 0:
                maxValue, minValue = minValue, maxValue
            
            maxValue = max(maxValue*nums[i], nums[i])
            minValue = min(minValue*nums[i], nums[i])

            answer = max(answer, maxValue)
        
        return answer
        



        

        

