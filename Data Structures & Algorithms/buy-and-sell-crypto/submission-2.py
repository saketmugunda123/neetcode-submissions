class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Simple sliding window problem where the window represents all the possible buy and sell values at a particular stock value. Remember, you can only consider selilng in an index position that is AFTER your current index. 
        # That means, whenever you encounter a smaller number than your current start point, then you can just move over to that number wihtout checking anything you skipped

        left = 0 
        answer = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                answer = max(answer, prices[right] - prices[left])
        return answer

        