class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #basically you process each node in teh for loop. the for loop iterates over
        #the curent len of the queue which represents the minute we are in. 
        #Ex: we start with 2 rotten oranges at minute 0. We iterate over len = 2
        #and then process those values. Now whatever values are left in the queue 
        #represent minute 1 and you then iterate over the len of queue again.

        from collections import deque

        def isValid(x,y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            return True

        #first find inital q values and num fresh fruit
        q = deque()
        freshFruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    freshFruit +=1
     
        
        minutes = 0
        seen = set()
        while q and freshFruit > 0:
            freshFruitFound = False
            for i in range(len(q)):
                currX, currY = q.popleft()
                seen.add((currX, currY))

                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dx,dy in directions:
                    newX, newY = dx + currX, dy + currY
                    if isValid(newX, newY) and (newX, newY) not in seen and grid[newX][newY] == 1:
                        freshFruitFound = True
                        freshFruit -=1
                        grid[newX][newY] = 2
                        q.append((newX,newY))
            minutes +=1
            if freshFruit == 0:
                return minutes
            elif not freshFruitFound:
                return -1
        return minutes if freshFruit == 0 else -1
            
                        






