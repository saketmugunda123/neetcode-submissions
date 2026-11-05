class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #Sort the array
        #Have a curr pointer, left pointer, and right pointer
        #Increment left if currSum < target and right otherwise
        #Once you find a solution, you have increment left so its at a new
        #value

        nums.sort()

        if len(nums) < 3:
            return []

        print(nums)
        left = 1
        right = len(nums) -1
        answerArr = []
        for i in range(0, len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            left = i + 1
            right = len(nums) -1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum < 0:
                    left +=1
                elif currSum > 0:
                    right -=1
                else:
        
                    answerArr.append([nums[i], nums[left], nums[right]])

                    #Only checks for duplicates (need to increment pointers)
                    while nums[left] == nums[left + 1] and left < len(nums) -2:
                        left +=1
                    
                    while nums[right] == nums[right -1] and right > 0:
                        right -=1
                    
                    #incrementing pointers forward
                    left +=1
                    right -=1

        return answerArr







