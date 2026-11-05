class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #first find what row it is in (iterate through col 0)

        #once you find row iterate through the row's corresponding columns


        #finding row
      
        top = 0
        bottom = len(matrix) -1

        #Trying to find the correct row
        while top <= bottom:
            row = (top + bottom) //2

            if target > matrix[row][-1]: #Last value of row
                top = row + 1
            elif target < matrix[row][0]: #First value of row 
                bottom = row - 1 
            else: #Found the right row
                break
        
        if top > bottom: #Occurs when target it greater than everything or else than everything
            return False
        
        rowVal = (top + bottom) //2
        
        #finding the correct col value
        left = 0 
        right = len(matrix[0])-1

        while left <= right:
            
            mid = (left + right) //2

            if matrix[rowVal][mid] < target:
                left = mid + 1
            elif matrix[rowVal][mid] > target:
                right = mid - 1
            else:
                return True 
        
        return False
            

        