class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        def dfs(index):


            if index >= len(cost):
                return 0
            
            if index in memo:
                return memo[index]
            

            step1 = dfs(index + 1)
            step2 = dfs(index +2)

            memo[index] = min(step1, step2) + cost[index]

            return memo[index]
        
        return min(dfs(0), dfs(1))
            

        