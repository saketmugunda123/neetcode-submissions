class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #First reverse the rows. So the last row becomes first row, second to last row becomes
        #second row etc.

        start = 0
        end = len(matrix) -1

        while start < end:
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start +=1
            end -=1
        

        #Now the matrix is set up to easily transpose. What you do is a simple swap of 
        #row 0 and col 0. Once that is complete both are finalized. 
        #Then, you increment your top and left pointer to now transpose the inner rectangle

        #All you need to keep track of is starting poitn because you go in diff direction from that
        #point and swap those values

        top = 0
        left = 0

        #iterate over the number of diagonals or while left and top are valid values (same thing)
        for diagonal in range(0, len(matrix)):
            
            vertPointer = top
            horizPointer = left

            while vertPointer < len(matrix) and horizPointer < len(matrix):
                #swap values
                matrix[vertPointer][left], matrix[top][horizPointer] = matrix[top][horizPointer], matrix[vertPointer][left] 

                vertPointer +=1
                horizPointer +=1
            
            top +=1
            left +=1





        