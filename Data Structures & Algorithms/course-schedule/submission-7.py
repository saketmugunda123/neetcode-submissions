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

        if not prerequisites:
            return True


        graph = {}
        for pair in prerequisites:
            course, prereq = pair
            if prereq not in graph:
                graph[prereq] = [course]
            else:
                graph[prereq].append(course)

            if course not in graph:
                graph[course] = []
        print(graph)

        #compute the indegree dict of each node
        indegreeDict = defaultdict(int)
        for course in graph:
            for value in graph[course]:
                indegreeDict[value] += 1
        
        queue = deque()
        visited = set()
        for course in graph:
            if indegreeDict[course] == 0:
                queue.append(course)
        if not queue:
            return False
        
        while queue:
            currCourse = queue.popleft()
            visited.add(currCourse)
    
            for neighbor in graph[currCourse]:
                if neighbor not in visited:
                    indegreeDict[neighbor] -=1
                if indegreeDict[neighbor] == 0:
                    queue.append(neighbor)
        
        
        return len(visited) == len(graph)


        