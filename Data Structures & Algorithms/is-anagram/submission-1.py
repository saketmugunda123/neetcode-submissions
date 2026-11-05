class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Sort strings and compare

        countDictS = {}
        countDictT = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            if s[i] not in countDictS:
                countDictS[s[i]] = 1
            else:
                countDictS[s[i]] +=1
            
            if t[i] not in countDictT:
                countDictT[t[i]] = 1
            else:
                countDictT[t[i]] +=1

        return countDictS == countDictT