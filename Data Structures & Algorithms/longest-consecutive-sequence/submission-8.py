class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        answer = 0
        for i in range(len(nums)):

            if nums[i] - 1 in numSet:
                continue
            
            count = 0
            curr = nums[i]
            while curr in numSet:
                count += 1
                curr = curr + 1
            
            answer = max(answer, count)
        return answer
            
                
            


            