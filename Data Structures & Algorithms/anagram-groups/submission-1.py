class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #In your dicitonary store a tuple that represents the counts of the word
        #The corresponding value pair should be the words that have that specifc count
        

        anagramDict = defaultdict(list)

        for i in range(0, len(strs)):
            count = [0]*26

            for letter in strs[i]:
                index = ord(letter) - ord("a")
                count[index] += 1
            
            anagramDict[tuple(count)].append(strs[i])

        answerList = []
        for key in anagramDict:
            answerList.append(anagramDict[key])
        
        return answerList

            

        



        
        