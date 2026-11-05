class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1

        #Two pointers 
        while left < right:
            currL = numbers[left]
            currR = numbers[right]
            print(left, right)
            if currL + currR == target:
                return [left + 1, right + 1]
            elif currL + currR < target:
                left +=1
            else:
                right -=1
        
        return []
        