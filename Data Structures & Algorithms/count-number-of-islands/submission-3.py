class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        from collections import deque

        ROWS = len(grid)
        COLS = len(grid[0])

        #write a function to make sure a place is valid
        def validMove(x,y):
            if x >= ROWS or x < 0 or y >= COLS or y < 0:
                return False
            elif grid[x][y] == '0':
                return False
            return True



        #Write BFS. Note: once you visit a node, be sure to mark it as visited
        def BFS(x, y):

            q = deque()

            q.append((x,y))

            while q:
                currX, currY = q.popleft()
                grid[currX][currY] = '0' #Set node to visited

                directions = [(currX + 1, currY), (currX -1, currY), 
                (currX, currY + 1), (currX, currY + -1)]

                for x,y in directions:
                    if validMove(x, y):
                        q.append((x,y))
        

        counter = 0
        for i in range(0, ROWS):
            for j in range(0, COLS):
                if validMove(i, j):
                    BFS(i,j)
                    counter +=1
        
        return counter





                






