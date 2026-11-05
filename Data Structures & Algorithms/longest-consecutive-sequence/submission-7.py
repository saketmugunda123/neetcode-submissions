class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a set for O(1) lookup. The idea is that you check if n-1 exists within the set. If it dones't then you know you are at the bottom of a sequence so every other number apart of this sequence can be removed after we fully process that sequence.

        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            
            start = num
            potential = 0
            while start in numSet:
                start = start + 1
                potential +=1
            longest = max(longest, potential)
        return longest
                
            


            