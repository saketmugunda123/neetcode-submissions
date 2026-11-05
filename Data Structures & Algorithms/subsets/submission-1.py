class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #1. base case: there really isn't one for this problem
        #2. iterate through all nums in arr
        #3. can't repeat (keep track of start index)
        #4. undo the choice

        answer = []
        def backtrack(start, path):
            answer.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1,path)
                path.pop()
            return
        
        backtrack(0,[])
        return answer


        