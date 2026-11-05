class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        result = []

        currSubset = []

        def dfs(i):
            if i >= len(nums):
                #If you get to end of tree, return the subset
                result.append(currSubset.copy())
                return


            #Takes care of case of appending value to subset
            currSubset.append(nums[i])
            dfs(i + 1)

            #Takes care of case of not appending to subset
            currSubset.pop()
            dfs(i + 1)

            return
        
        dfs(0)
        return result
        


        