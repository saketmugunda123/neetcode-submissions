class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}

        #create graph
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        answerOrder = []
        visited = set()
#create the dfs function and keep track of visited set so we don't revist     nodes that we have already processed in other dfs paths (they are already in answerOrder)
        def dfs(course, path):
            if course in path:
                return False
            
            if course in visited:
                return True
            
            path.add(course)
            visited.add(course)
            
            for neighbor in graph[course]:
                answer = dfs(neighbor, path)
                if not answer:
                    return False
            answerOrder.append(course)
            path.remove(course)
            return True
        
        for course in graph:
            if not dfs(course, set()):
                return []
        return answerOrder



        