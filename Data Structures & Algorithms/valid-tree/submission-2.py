class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        #Create adjacency list
        adjDict = {}

        for edge in edges:
            if edge[0] not in adjDict:
                adjDict[edge[0]] = []

            if edge[1] not in adjDict:
                adjDict[edge[1]] = []
            
            adjDict[edge[0]].append(edge[1])
            adjDict[edge[1]].append(edge[0])
        
        print(adjDict)



        #A tree is simply a component without cycles
        visited = set()
        isTree = [True]
        def dfs(parentNode, currNode):

            if currNode in visited:
                isTree[0] = False
                return
            
            visited.add(currNode)

            for child in adjDict[currNode]:
                if child == parentNode:
                    continue
                dfs(currNode, child)
            return
 

        dfs(None, 0)
        return isTree[0] and len(visited) == n
        