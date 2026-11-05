class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #TOPOLOGICAL SORT

        # 1) Create the adjacency list and the indegrees array.

        indegrees = [0]*numCourses #The index in the array maps to the course
        adjList = [0]*numCourses

        for i in range(0, numCourses):
            adjList[i] = []
        

        for pair in prerequisites:
            print(adjList)
            course = pair[0]
            prereq = pair[1]

            #Increment the indegree
            indegrees[course] +=1

            adjList[prereq].append(course)
        
      
        # 2) Create the queue and start by adding all the values with indegree 0
      
        from collections import deque
        q = deque()

        for i in range(0, len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        
        if len(q) == 0:
            return False
        
        #Keep track of visited nodes already (for cycle detection)
        visited = set()

        #Now iterate while the q has values
        while q:
            currNode = q.popleft()
            visited.add(currNode)

            #Updating the indegrees of the neighboring nodes after deletion
            for neighbor in adjList[currNode]:
                indegrees[neighbor] -=1

                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        return len(visited) == numCourses








