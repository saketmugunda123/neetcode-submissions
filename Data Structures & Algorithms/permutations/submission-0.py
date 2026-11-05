class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #what makes permutations diff than subsets is that permutations allows for diff order, but it has to include every number (you are not just including every value)

        #1. base case- array of length 3 return the copy of the array

        #2. choices- over all numbers in the array (check 1 2 and 3)

        #3. constraints- only add numbers that are not in the path

        #4. backtracking- remove number from path continue. Remeber, the recrusion
        #takes you back tbe place where you go down a new path

        answer = []
        def backtrack(path):
            #base case
            if len(path) == len(nums):
                answer.append(path.copy())
                return
            
            #chocies
            for num in nums:
                if num in path:  #constraint
                    continue
            
                path.append(num)  #make choice
                backtrack(path)
                path.pop()  
            return
        
        backtrack([])
        return answer
            


        