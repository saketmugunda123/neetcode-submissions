class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a set for O(1) lookup. The idea is that you check if n-1 exists within the set. If it dones't then you know you are at the bottom of a sequence so every other number apart of this sequence can be removed after we fully process that sequence.

        setNums = set(nums)
        maxLength = 0
        for i in range(0, len(nums)):

            if nums[i] not in setNums:
                continue

            if (nums[i] - 1) in setNums:
                continue
            
            sequence = 0
            conditionNum = nums[i]
            while conditionNum in setNums:
                sequence +=1
                setNums.remove(conditionNum)
                conditionNum += 1
            
            maxLength = max(maxLength, sequence)
        
        return maxLength