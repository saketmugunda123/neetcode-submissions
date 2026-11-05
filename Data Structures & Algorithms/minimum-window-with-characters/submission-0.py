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
            if t[i] not in targetDict:
                targetDict[t[i]] = 1
            else:
                targetDict[t[i]] +=1
        


        currWindow = {}

        left = 0
        result = []

        for right in range(0,len(s)):
            
            #Adding s[right] to the currWindow
            if s[right] not in currWindow:
                currWindow[s[right]] = 1
            else:
                currWindow[s[right]] +=1

            #while valid window you want to increment left bc you are trying to find smallest window
            while all(currWindow.get(c, 0) >= targetDict[c] for c in targetDict):
                result.append([left, right, right - left +1])
                currWindow[s[left]] -= 1
                left +=1

        if not result:
            return ""

        best = min(result, key=lambda x: x[2])

        return s[best[0]:best[1]+1] #include last character in window



            

        
        

 

