class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        #Iterate through array and append to dictionary if 
        #combo of characters hasn't been seen

        #Append combos to array by sorting the string input

        #Getting the dictionary {"sorted str": List of strings}
        stringsDict = {}
        for i in range(0, len(strs)):
            currString = sorted(strs[i])
            currString = "".join(currString)

            if currString not in stringsDict:
                stringsDict[currString] = [strs[i]]
            else:
                stringsDict[currString] += [strs[i]]

        answerList = []
        for key in stringsDict:
            answerList.append(stringsDict[key])

        return answerList
        



        
        