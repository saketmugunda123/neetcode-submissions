class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #the idea is that for each index, you keep it constant and then run 2 pointers (the 2sum II solution) on the reminaing array to get O(n^2)
    
        answerArr = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) -1
            target = 0 - nums[i]
            while j < k:
                currSum = nums[j] + nums[k]
                
                if currSum > target:
                    k -=1
                elif currSum < target:
                    j +=1
                else:
                    print(i, j, k)
                    answerArr.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j -1] == nums[j]:
                        j += 1


        return answerArr
                        

                    
                
        