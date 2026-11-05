class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Use a set for easy lookup
        setNums = set(nums)

        visited = set()

        if len(nums) == 0:
            return 0

        answer = 0
        for num in nums:
            if num in visited:
                continue

            length = 1
            visited.add(num)
            while (num + 1) in setNums:
                length +=1
                visited.add(num + 1)
                num = num + 1

            answer = max(answer, length)
        
        return answer
            

            

            
            
            

        
    

        


            
            
            

