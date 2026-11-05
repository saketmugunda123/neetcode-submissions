class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #In the list index 1 points to 0 in the graph

        #We will do an indegree method where we compute the indegrees of each value
        #Whatever value has an indegree of 0 we will start with them 
        #We know that we can perform the entire scheudle if we end up visitng 
        #every node. However, if we run into a cycle, then there will end up being
        #unvisited nodes (bc their indegrees will never be 0)

        #build the adajency map
        from collections import defaultdict
        from collections import deque


        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for pair in prerequisites:
            course, prereq = pair
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        visited = set()
        for course in graph:
            if indegree[course] == 0:
                queue.append(course)
    
        while queue:
            currCourse = queue.popleft()
            visited.add(currCourse)
    
            for neighbor in graph[currCourse]:
                if neighbor not in visited:
                    indegree[neighbor] -=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        
        return len(visited) == len(graph)


        