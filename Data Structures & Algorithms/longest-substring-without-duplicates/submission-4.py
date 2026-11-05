class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Basically use a set to maintain what current characters in window

        #If set length doesn't increase (not same size as window), 
        #then its an invalid window

        #Remove s[left] from set until the set is valid again
        # len(set) == right - left + 1

        left = 0
        currSet = set()
        answer = 0
        for right in range(0,len(s)):

            #if set is not valid
            while s[right] in currSet:
                currSet.remove(s[left])
                left +=1
            
            currSet.add(s[right])
            answer = max(answer, right - left + 1)
        
        return answer
            


                
            


        