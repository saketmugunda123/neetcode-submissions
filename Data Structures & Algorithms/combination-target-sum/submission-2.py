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
                

            #Add nums[i] to the curr array
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            
            #Now remove it once you have went all the way with that one num
            curr.pop()

            #Recursive step
            dfs(i+1, curr, total)
    

        
        dfs(0, [], 0)
        return self.result

