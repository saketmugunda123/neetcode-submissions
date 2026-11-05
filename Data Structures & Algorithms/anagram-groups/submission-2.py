class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #figure out the count of each word and store in 26 len tuple. Then append each 26 len tuple to the dict. The reason we use tuples is because they are immutable so they can be keys in the dictionary

        
        wordDict = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                count[index] +=1
            count = tuple(count)
            
            if count not in wordDict:
                wordDict[count] = [word]
            else:
                wordDict[count].append(word)
        
        return list(wordDict.values())





