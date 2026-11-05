class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        #Store the +1 of a number in a dictionary and the number as the key

        numsDict = {}

        for i in range(0, len(nums)):
            numsDict[nums[i]] = nums[i] + 1
        


        keys = set(numsDict.keys())
        longest = 0
        visited = set()
        for key in numsDict:
            curr = 0
            if key in visited:
                continue
            
            visited.add(key)
            condition = True
            while condition:
                curr +=1
                if numsDict[key] not in keys:
                    condition = False
                
                key = numsDict[key]
                visited.add(key)
        
            longest = max(curr, longest)
        
        return longest
    

        


            
            
            

