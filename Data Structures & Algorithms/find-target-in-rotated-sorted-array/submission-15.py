class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #The idea is to first find the pivot through binary search
        #Once you find the pivot, you have 2 sorted arrays (1 before pivot and 1 after)
        #Determine which array target is in and then search that array


        #Finding pivot
        left = 0
        right = len(nums) -1

        while left < right:
            mid = (left + right)//2

            #Left is the pivot (our current section is sorted)
            if nums[left] < nums[right]:
                break
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        #Finding the correct array
        leftSearch = 0
        rightSearch = len(nums) -1

        if nums[pivot] == target:
            return pivot

        if target >= nums[pivot] and target <= nums[rightSearch]:
            leftSearch = pivot
        else:
            rightSearch = pivot -1
        


        print(pivot)
        print(leftSearch, rightSearch)
        while leftSearch <= rightSearch:

            mid = (leftSearch + rightSearch)//2

            if target > nums[mid]:
                leftSearch = mid + 1
            elif target < nums[mid]:
                rightSearch = mid -1
            else:
                return mid
        
        return -1

            
