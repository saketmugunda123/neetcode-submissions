class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #Create the whole tree. You will traverse it like normal. However, as you traverse, once you
        #find the best way to make a coin from a particular "amount", you store it in the cache.
        #when you then find that same value again in the tree, you can just return the compuation you
        #already did



        #First I am going to write the regular recursive solution (no memoizaiton)
        memo = {}
        def dfs(amount):

            #from amount == 0, you need 0 coins to get to 0
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]

            #Going down each tree
            answer = float('inf')
            for coin in coins:
                
                if amount - coin >= 0:
                    result = dfs(amount - coin)
                    answer = min(answer, 1 + result)
            
            memo[amount] = answer

            return answer
        

        return dfs(amount) if dfs(amount) != float('inf') else -1
            
            





            





