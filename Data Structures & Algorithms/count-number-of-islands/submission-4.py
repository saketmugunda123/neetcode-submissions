class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        def bfs(start):
            queue = deque()
            queue.append(start)
            visited.add(start)
            while queue:
                row, col = queue.popleft()
                
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1' and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
        
        
        numIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == '1':
                    bfs((row,col))
                    numIslands +=1
        return numIslands




            
            


