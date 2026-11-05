class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #figure out the count of each word and store in 26 len tuple. Then append each 26 len tuple to the dict. The reason we use tuples is because they are immutable so they can be keys in the dictionary

        
        wordDict = {}
        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord("a")] +=1
            tupleCount = tuple(count)
            if tupleCount not in wordDict:
                wordDict[tupleCount] = [word]
            else:
                wordDict[tupleCount].append(word)
        
        answerArr = []
        for word in wordDict:
            answerArr.append(wordDict[word])
        return answerArr





