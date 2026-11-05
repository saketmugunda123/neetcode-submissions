class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #Idea: Do BFS on each occurance of land. The trick here is that
        #Once you visit a island, you mark all the land surrounding that island
        #as visited. Then you start BFS on the next unvisited island

        #You know you have found an island when the queue is empty
        #Because you only append land items to the queue
        #If there is no land to continue to from a certain location, then return


        #valid move
        def validMove(x, y):
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
                return False
            elif grid[x][y] == '0' or grid[x][y] == '#': #Placeholder for visited       
                return False
            return True
        

        #Writing the actual BFS
        from collections import deque

        def bfs(x,y):
            queue = deque()
            queue.append((x,y))

            while queue:
                currX, currY = queue.popleft()

                directions = [(currX + 1, currY), (currX - 1, currY),
                (currX, currY + 1), (currX, currY -1)]

                for tempX, tempY in directions:
                    if validMove(tempX, tempY):
                        queue.append((tempX, tempY))
                        grid[tempX][tempY] = '#'
        
        counter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    bfs(x,y)
                    counter +=1
                    print(grid)
        
        return counter
                






