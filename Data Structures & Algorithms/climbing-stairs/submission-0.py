class Solution:
    def climbStairs(self, n: int) -> int:

        #Solve this with recursion
        #Basically at each step, pick between going up 1 step and then 2 steps
        #Base cases are you are equal to n or you are greater than n
        #Then backtrack back to the last valid step


        def dfs(currSum, counter):

            #Base cases
            if currSum == n:
                counter +=1
                return counter
            
            if currSum >= n:
                return 0
            
            #Go up 1 step and then 2 steps
            oneStep = dfs(currSum + 1, counter)
            twoStep = dfs(currSum + 2, counter)
            return oneStep + twoStep
        
        
        return dfs(0, 0)

            

        