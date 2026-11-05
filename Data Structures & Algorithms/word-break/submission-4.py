class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        #Write the recursive solution first
        #Idea: basically the tree breaks off from the indexes. FOr example, at index 0, you check 
        #if any of the words are valid. If they are, you can descend down that path

        #Meomizaiton: lets say from index[5], you know the answer can't be acheived. That means
        #store that dp[5] = False, so when you run into index = 5, you don't have to descend tree

        dp = {}

        def bruteForce(index):

            if index in dp:
                return False

            if index == len(s):
                return True
            

            for word in wordDict:
                if word == s[index: index + len(word)]:
                    path = bruteForce(index + len(word))

                    if path:
                        return True
                    else:
                        dp[index] = False
            return False
        
        return bruteForce(0)
            


            
