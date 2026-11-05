class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        #Idea: Do DFS and return left + right + up + down. This'll tell you
        #How many cells there are 
        #Your base case occurs when you reach a 0, visited node, or edge

        def dfs(x, y):

            #if out of bounds
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                return 0 #Invalid node
            
            if grid[x][y] == '#' or grid[x][y] == 0:
                return 0
            
            grid[x][y] = '#' #Setting node as visited

            left = dfs(x, y-1)
            right = dfs(x, y+1)
            up = dfs(x-1, y)
            down = dfs(x+1, y)

            return 1 + right + left + up + down  #One represents curr node
        
        #area counter
        area = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                if grid[x][y] == 1:     
                    area = max(area, dfs(x,y))
        return area
        
