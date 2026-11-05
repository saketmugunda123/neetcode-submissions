class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.result = []
        
        def dfs(i, curr, total):

            #Create base cases
            # 1) Out of bounds
            # 2) equal to sum
            # 3 ) go over sum

            if i >= len(nums):
                return
            

            if total == target:
                self.result.append(curr.copy())
                return

            if total > target:
                return
                

            
            #add nums[i] to the curr array
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            #when we get here means that we have went as far as we can with that number
            curr.pop()

            #This step is simply to get toward the next value (next index)
            dfs(i+1, curr, total)

    

        
        dfs(0, [], 0)
        return self.result

