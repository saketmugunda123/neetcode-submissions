class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        #THis function checks if r and c are in bounds
        def inBounds(i, j, board):
            if not board or not board[0]: 
                return False
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        #Keeps track of the current path
        path = set()     
        


        def dfs(r,c,index):
            if index == len(word):
                return True
            if not inBounds(r, c, board):
                return False
            if word[index] != board[r][c]:
                return False
            if (r,c) in path:
                return False
            
            path.add((r,c))
            result = (
            dfs(r+1, c, index+1) or
            dfs(r-1, c, index+1) or
            dfs(r, c+1, index+1) or
            dfs(r, c-1, index+1)
            )

            path.remove((r,c))
            return result
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        

        return False

