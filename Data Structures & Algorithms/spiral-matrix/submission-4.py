class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        #Have a left, right, top, and bottom pointer that serve as bounds
        #After each circle you complete, you update these bounds
        #The bounds create a new rectangle that you complete in the same manner

        left = 0
        right = len(matrix[0]) #note its not len(matrix) -1 bc the code is eaiser (you'll see)

        top = 0
        bottom = len(matrix) #same reasoning as for right

        result = []

        #The exit condition occurs when left == right or top == bottom
        while left < right and top < bottom:
            print('hello')
            #left to right of top row
            for i in range(left, right):
                result.append(matrix[top][i])
            
            top +=1 #now update top bound (+=1) after getting the top row values

            #This check is necessary bc while the next for loop woudlnt run, if left and right
            # are still apart, then more values will be added (3rd for loop). Remember, the rect is valid if
            #BOTH left < right AND top < bottom.
            if top >= bottom:
                break

            #right column
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            
            right -=1 #change the right bound now that we have completed that column

            #Same concept as above but this now applies when you have a column remaining as opposed 
            #to a row remaining
            if left >= right:
                break
            
            #bottom row
            for i in range(right -1, left -1, -1):
                result.append(matrix[bottom-1][i])
            
            bottom -= 1 #finished bottom row

            #left column
            for i in range(bottom -1, top -1, -1):
                result.append(matrix[i][left])
            left +=1

        
        return result


            



        