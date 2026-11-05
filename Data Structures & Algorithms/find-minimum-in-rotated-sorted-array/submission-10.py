class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # #Your goal is to find the split (where the array breaks sorted trend)
        # #You know 2 of l, m, and r will be sorted
        # # If l and m are sorted, go toward r 
        # # If m and r are sorted, go toward l

        # left = 0
        # right = len(nums) - 1
        # result = float('inf')
        # while left <= right:

        #     if nums[left] <= nums[right]: #In a sorted subarray
        #         result = min(result, nums[left])
        #         break
            
        #     #Find which subarray to explore (left or right)
        #     #Move toward opposite subarray
        #     mid = (left + right)//2
        #     #Update result at each iteration to make sure we don't accidentally
        #     #skip it
        #     result = min(result, nums[mid])

        #     if nums[mid] >= nums[left]:
        #         left = mid + 1
        #     else:
        #         right = mid -1
        
        # return result

        answer = float('inf')
        left = 0
        right = len(nums) -1 
        
        while left <= right:
            
            mid = (left + right)//2
            print(mid)

            if nums[left] <= nums[right]:
                return nums[left]

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[mid]