class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #Subproblem: The LIS[i] = 1 + max(LIS[i+1] .. LIS[len(nums-1)])
        # you are only able to change LIS[i] if nums[i] < nums[i +1]
        #at the end return the max of the LIS array

        LIS = [1]*len(nums)

        #Start at the second to last index:
        for i in range(len(nums) -2 , -1, -1):
            localMax = 1
    
            for j in range(i + 1, len(nums)):

                if nums[i] < nums[j]:
                    localMax = max(localMax, LIS[j])
                    LIS[i] = max(LIS[i], localMax + 1)
            

        return max(LIS)





        