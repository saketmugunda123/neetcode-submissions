class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #Build the adj list
        adjList = [0]*n
        
        for i in range(0,n):
            adjList[i] = []


        for edge in edges:
            first = edge[0]
            second = edge[1] 
            
            adjList[first].append(second)
            adjList[second].append(first)
        
        
        #Create the dfs function to run on each node
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in adjList[node]:
                dfs(neighbor)
        

        #Run dfs on each node if they haven't been visited yet
        numComponents = 0
        for i in range(0,n):
            if i not in visited:
                dfs(i)
                numComponents +=1
        
        return numComponents






