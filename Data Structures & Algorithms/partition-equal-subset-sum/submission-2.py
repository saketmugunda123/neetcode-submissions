class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        answerArr = []

        memo = {}
        if totalSum == 0:
            return True
        

        def dfs(index, currSum):

            if index >= len(nums):
                return False 

            if currSum in memo:
                return False

            currSum += nums[index]
            
            if totalSum - currSum == currSum:
                return True
            
            left = dfs(index + 1, currSum)

            currSum -= nums[index]
            right = dfs(index + 1, currSum)

            memo[currSum] = -1

            return left or right
        
        return dfs(0,0)




        


        