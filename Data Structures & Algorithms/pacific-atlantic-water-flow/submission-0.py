class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #Idea: So the goal is to do start in the oceans and then see how many
        #Nodes you can visit from the ocean.

        #That way you only need to run dfs on the outer values bc they are connected
        #To the oceans

        #Initalize your sets
        pacific = set()
        atlantic = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        #The goal of the dfs is to fill out the sets
        def dfs(row,col,visitSet, prevHeight):
            if row == ROWS or col == COLS or row < 0 or col < 0:
                return
            
            #This is because we are going backwards (going from ocean to nodes)
            if prevHeight > heights[row][col]:
                return

            if (row,col) in visitSet:
                return
            #Means that the node can visit the corresponding ocean (depending
            # on the set being used)
            visitSet.add((row,col))

            dfs(row+1, col, visitSet, heights[row][col])
            dfs(row-1, col, visitSet, heights[row][col])
            dfs(row, col+1, visitSet, heights[row][col])
            dfs(row, col-1, visitSet, heights[row][col])
        

        #Checking the top row and bottom row
        for c in range(0,COLS):
            dfs(0, c, pacific, 0) #The top row is associated with pacific ocean
            dfs(ROWS-1,c, atlantic, 0) #Bottom row with atlantic ocean
        

        for r in range(0,ROWS):
            dfs(r,0, pacific, 0)
            dfs(r, COLS-1, atlantic, 0)

        
        answerArr = []
        for r in range (0,ROWS):
            for c in range (0,COLS):
                if (r,c) in atlantic and (r,c) in pacific:
                    answerArr.append([r,c])
        
        return answerArr



        
        