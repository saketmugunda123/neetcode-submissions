class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #basically you process each node in teh for loop. the for loop iterates over
        #the curent len of the queue which represents the minute we are in. 
        #Ex: we start with 2 rotten oranges at minute 0. We iterate over len = 2
        #and then process those values. Now whatever values are left in the queue 
        #represent minute 1 and you then iterate over the len of queue again.

        from collections import deque

        #idea: keep track of levels of BFS (that corresponds to minutes)
        #we keep track of levels by iterating over length of queue
        #also need to keep a count of freshfruit

        freshFruit = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshFruit +=1
                elif grid[i][j] == 2:
                    q.append((i,j))

        if freshFruit == 0:
            return 0
        
        def isValid(x,y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return False
            return True
        
        seen = set()
        minutes = 0

        while q:
            for i in range(len(q)):
                currX, currY = q.popleft()
                seen.add((currX, currY))
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dx, dy in directions:
                    newX, newY = currX + dx, currY + dy
                    if isValid(newX, newY) and grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        freshFruit -=1
                        q.append((newX,newY))
            minutes +=1
            if freshFruit == 0:
                return minutes
        return -1
        

                

        
                        






