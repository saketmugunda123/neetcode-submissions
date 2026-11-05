class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #Base case- sum of values equals target return the path
        #Choices- loop over every value in the array
        #Constraint- if we go over the sum 
        #Backtrack- undo the choice

        nums.sort()
        answer = []
        def backtrack(start, currSum, path):
        
            #base case
            if currSum == target:
                answer.append(path.copy())
                return

            for i in range(start, len(nums)):
                if currSum + nums[i] > target:
                    break
                currSum += nums[i]
                path.append(nums[i])
                backtrack(i, currSum, path) 
                currSum -= nums[i]
                path.pop()
            return
        backtrack(0,0,[])
        return answer

    #The reason we need start is because 
            


        