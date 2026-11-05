class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #the main bottleneck with this problem is figuring out how to prase the 3x3 boxes.
        #An idea I had for determining the 3x3 boxes is having a funciton that checks the 3x3 boxes and the thing we pass into it is the starting point (top left corner)

        #this whole section is for checking boxes
        def boxCheck(start):
            x,y = start
            seen = set()  
            for i in range(3):
                for j in range(3):
                    currNum = board[x+i][y+j]
                    if currNum == ".":
                        continue
                    if currNum in seen:
                        return False
                    seen.add(currNum)
            return True

        # start = [0,0]
        # while (start[0] < 9):
        #     if boxCheck(start):
        #         start[1] +=3
        #         if start[1] == 9:
        #             start[0] += 3
        #             start[1] = 0
        #     else:
        #         return False

        #The box chekcing loop can be written as such (using increment parameter)
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not boxCheck([i,j]):
                    return False
        

        #checking each row
        rowSet = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
            rowSet.clear()
        
        #checking each column
        colSet = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in colSet:
                    return False
                colSet.add(board[j][i])
            colSet.clear()
        return True


                
        

                

        
        



        