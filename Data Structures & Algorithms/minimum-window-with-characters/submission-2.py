class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #Idea: Create a targetdict which simply represents the t string.
        #First expand the window until you it becomes invalid
        #Then, increment l pointer until invalid window

        #Key: a window (a dict) is considered valid if its counts are >= to the counts in targetDict


        #Create targetDict
        #Note: To create targets dict, you can from collections import Counter
        # targetDict = Counter(t)

        targetDict = {}

        for i in range(0, len(t)):
            #counts.get returns that value at the specified key. THe ,0 simply returns 0 if key isn't found
            targetDict[t[i]] = 1 + targetDict.get(t[i], 0)
        


        currWindow = {}
        have, need = 0, len(targetDict)
        print(need)
        left = 0
        result = [-1,-1]
        resultLen = float('infinity')

        for right in range(0,len(s)):
            
            #Adding s[right] to the currWindow
            currLetter = s[right]
            currWindow[currLetter] = 1 + currWindow.get(currLetter,0)

            #Checking if currLetter is in the targetDict and seeing if we have met a condition
            if currLetter in targetDict and currWindow[currLetter] == targetDict[currLetter]:
                have +=1
            
            #When have == need, we have a valid window. So now, we have to decrease windown until invaild
            while have == need:

                #Seeing if we should update result
                if right - left + 1 < resultLen:
                    result[0], result[1] = left, right
                    resultLen = right - left + 1
                   
                
                #Removing left most character of window
                currWindow[s[left]] -= 1

                #Now we have to check if have and need conditions have updated
                if s[left] in targetDict and currWindow[s[left]] < targetDict[s[left]]:
                    have -= 1 #We have now lost one of the conditions

                left +=1

        leftBound, rightBound = result[0], result[1]
        if resultLen < float('infinity'):
            return s[leftBound:rightBound+1]
        else:
            return "" 


            

        
        

 

