class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()  # Step 1: Sort the array
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate fixed elements

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Step 3: Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result
