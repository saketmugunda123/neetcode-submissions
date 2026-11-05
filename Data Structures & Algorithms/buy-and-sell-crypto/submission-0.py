class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Have a left and right pointer
        # If left is greater than right, increment left to where right
        #If not continue updating the answer value

        left = 0
        answer = 0
        for right in range(1, len(prices)):

            #Incrementing left to make sure you get a profit
            while left < right and prices[left] > prices[right]:
                left +=1
            
            answer = max(answer, prices[right]- prices[left])
        
        return answer
            
