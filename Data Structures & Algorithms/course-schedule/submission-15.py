class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #In the list index 1 points to 0 in the graph

        #We will do an indegree method where we compute the indegrees of each value
        #Whatever value has an indegree of 0 we will start with them 
        #We know that we can perform the entire scheudle if we end up visitng 
        #every node. However, if we run into a cycle, then there will end up being
        #unvisited nodes (bc their indegrees will never be 0)


        #DFS SOLUTION: Run DFS on every node. If you can reach every node, then good.
        #If you run into cycle (visit same node in path), then return false

        #build the adajency map
        graph = {i: [] for i in range(numCourses)}
        
        for course,prereq in prerequisites:
            graph[course].append(prereq)


        def dfs(course, path):
            if course in path:
                return False
            
            if graph[course] == []:
                return True
            
            path.add(course)
            for neighbor in graph[course]:
                answer = dfs(neighbor,path)
                if not answer:
                    return False
            path.remove(course)
            graph[course] = [] #Don't ever need to check this node again on any path
            return True #if we make it out recursive loop, we are good
        
        for course in graph:
            if not dfs(course, set()):
                return False

        return True

                

        


        