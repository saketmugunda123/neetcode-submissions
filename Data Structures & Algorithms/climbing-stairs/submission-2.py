class Solution:
    def climbStairs(self, n: int) -> int:
        #recurrence relation: f(n) = f(n + 1) + f(n + 2)

        if n < 2:
            return n

        memo = [0]*n
        memo[n-1] = 1
        memo[n-2] = 2
        for i in range(n-3, -1, -1):
            memo[i] = memo[i + 1] + memo[i + 2]
        
        return memo[0]

            
        