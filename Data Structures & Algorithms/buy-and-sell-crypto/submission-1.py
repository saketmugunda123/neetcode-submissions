class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        answer = 0
        for right in range(1, len(prices)):

            if prices[left] < prices[right]:
                answer = max(answer, prices[right]-prices[left])
            else:
                left = right
        
        return answer

            
