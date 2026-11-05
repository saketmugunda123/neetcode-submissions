class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Base case
        if not nums:
            return -1
            
        # Find the pivot (smallest element)
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # left is now the pivot
        pivot = left
        
        # Decide which segment to search
        left, right = 0, len(nums) - 1
        
        # Determine which half to search
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot #Search right side of array
        else:
            right = pivot-1  #search left side of array
        
        # Standard binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1