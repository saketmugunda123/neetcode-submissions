class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #recurrence relation: LIS(n) = max(LIS from n + 1 to end of arr))
        #This is an n^2 solution bc you check over every occurrence after the one you are currently at. The best LIS at index i is the max of t

        if len(nums) < 2:
            return len(nums)

        n = len(nums)
        memo = [0]*n
        memo[n-1] = 1
        for i in range(n-2, -1, -1):
            maxVal = 1
            for k in range(i+1, n):
                if nums[i] < nums[k]:
                    maxVal = max(maxVal, memo[k] + 1)
            memo[i] = maxVal
        return max(memo)
        