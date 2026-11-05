class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        
        def dfs(i, curr, total):

            #This occurs when you find a combination that is correct
            if total == target:
                result.append(curr.copy())
                return

            #This occurs when you exceed target OR i is out of bounds
            #When i is out of bounds, that means that you have no other valid 
            #values to check. 
            if i >= len(nums) or total > target:
                return
            

            #2 cases 
            #1) We include the current index as a potential candidate Ex:
            #adding nums[i] over and over again
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            #2) We get to a point where nums[i] + nums[i] ... + nums[i] reaches
            #a base case so now, along this path, have to try a new number
            #which is nums[i + 1]
            curr.pop() #Get rid of the value we just appended
            dfs(i+1, curr, total) #Iterate to next num
        
        dfs(0, [], 0)
        return result


       