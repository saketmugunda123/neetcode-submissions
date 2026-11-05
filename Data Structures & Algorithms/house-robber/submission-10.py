class Solution:
    def rob(self, nums: List[int]) -> int:
        #Recurrence relation: f(n) = max(f(n+1), nums[i] + f(n + 2))
        #The trick is that you have to run this on f(0) and f(1) and return the max 
        #The reason is bc if you only run this on f(n) you never consider any posibilites with f(1) being int eh solution

        if len(nums) < 2:
            return max(nums)
        
        n = len(nums)
        memo = [0]*(n)
        memo[n-1] = nums[n-1]
        memo[n-2] = max(memo[n-1],nums[n-2])

        for i in range(n-3,-1,-1):
            memo[i] = max(nums[i]+memo[i+2], memo[i+1])
        return memo[0]

        