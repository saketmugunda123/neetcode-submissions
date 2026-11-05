class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        #THis function checks if r and c are in bounds
        def inBounds(i, j, board):
            if not board or not board[0]: 
                return False
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        #Keeps track of the current path
        path = set()     
        
        #index represents the letter you are currently checking in the word
        def dfs(r, c, index): 

            #Base cases

            if (r,c) in path: #Makes we don't go back to the previous value in path
                return False

            if index == len(word):
                return True #if we get thorugh the whole word without errors, return true

            if not inBounds(r,c, board):
                return False

            elif board[r][c] != word[index]:
                return False

            
            #add the curr letter to path
            path.add((r,c))

            #check each direction
            down = dfs(r + 1, c, index + 1)
            up = dfs(r -1, c, index + 1)
            left = dfs(r, c -1, index + 1)
            right = dfs(r, c + 1, index + 1)

            path.remove((r,c))

            return down or up or left or right

        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                answer = dfs(i,j, 0)
                if answer:
                    return True
        
        return False



