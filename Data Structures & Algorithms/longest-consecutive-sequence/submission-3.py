class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Create a set for nums for O(1) look up

        #To actually lookup into the set, you need to make sure you are
        #at the start of a sequence

        #have a answer var that updates as you iterate through nums

        numsSet = set(nums)
        answer =0
        length = 0
        for num in nums:

            #If num isn't start of sequence, continue
            if num -1 in numsSet:
                continue
            
            length = 1
            counter = 1
            while num + counter in numsSet:
                length +=1
                counter +=1
            
            answer = max(answer, length)
        
        return answer
        
            





            

            
            
            

        
    

        


            
            
            

