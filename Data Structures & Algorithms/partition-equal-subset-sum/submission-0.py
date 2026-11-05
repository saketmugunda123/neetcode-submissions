class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        answerArr = []
        if totalSum == 0:
            return True

        def dfs(index, currArr):

            if index >= len(nums):
                return False 

            currArr.append(nums[index])
            

            if totalSum - sum(currArr) == sum(currArr):
                return True
            
            left = dfs(index + 1, currArr)

            currArr.remove(nums[index])
            right = dfs(index + 1, currArr)

            return left or right
        
        return dfs(0,[])




        


        