class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Simply just use a dictionary to count up the occurrances of each number
        #The reason this is O(1) space is because the dictionary can be at max 26 keys

        sDict = {}
        tDict = {}

        for letter in s:
            if letter not in sDict:
                sDict[letter] = 1
            else:
                sDict[letter] +=1
        
        for letter in t:
            if letter not in tDict:
                tDict[letter] = 1
            else:
                tDict[letter] +=1

        return sDict == tDict
        
