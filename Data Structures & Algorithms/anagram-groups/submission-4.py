class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        
        countsDict = defaultdict(list)

        for word in strs:
            wordCount = [0]*26
            for letter in word:
                index = ord(letter) - ord('a')
                wordCount[index] +=1
            countsDict[tuple(wordCount)].append(word)

        return [value for value in countsDict.values()]



