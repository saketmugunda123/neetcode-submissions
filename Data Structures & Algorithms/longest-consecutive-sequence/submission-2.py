class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        answer = 0

        for num in nums:
            length = 0
            #Don't start the checking process if it isn't the start of a sequence
            if (num -1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length +=1
            answer = max(length, answer)
        
        return answer


            

            
            
            

        
    

        


            
            
            

