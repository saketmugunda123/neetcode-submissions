class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #Find minimum in rotated sorted array

        #The goal is to find the pivot (where the numbers go from increasing to decreasing)

        #Idea: of left, mid, and right, two of them are sorted and one isn't. Move toward unsorted side

        #Ex: [3,4,5,6,1,2] l=3, m=5, and r=2. Move toward r=2 so adjust left and continue

        left = 0
        right = len(nums) -1

        while left < right:

            mid = (left + right)//2

            #If the current array in our scope is sorted, then we can just return minimum (nums[left])
            if nums[left] < nums[right]:
                return nums[left]
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
            

        return nums[left]

                
    