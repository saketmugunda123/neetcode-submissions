class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        def dfs(index):

            
            if index == len(s):
                return 1  #Found a valid way

            if s[index] == '0':
                return 0 #no character can start with 0
            
            if index in memo:
                return memo[index]
        
            count = dfs(index+1) #If s[index] not 0 (which we check before), its valid

            if(index + 1 < len(s)) and ((s[index]== "1") or (s[index] == "2" and s[index+1] in "0123456")):
                count += dfs(index + 2)


            memo[index] = count
            return count

        return dfs(0)
            
            

            






            
       




        