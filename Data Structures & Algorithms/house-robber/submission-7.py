class Solution:
    def rob(self, nums: List[int]) -> int:

        answer = 0

        #Start at the end of the array. Update nums[i] = nums[i] + nums[i+2]
        #nums[i+2] represents the best possible answer assuming the array starts at i+2

        #After this for loop, nums[i] will have the best case at that value
        for i in range(len(nums)-3, -1, -1):
                nums[i] = max(nums[i] + nums[i+2], nums[i+1])
        
        return max(nums)
            
            



        