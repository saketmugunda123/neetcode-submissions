class Solution:

    #The goal of this problem is to figure out how to determine where a list breaks
    #and put that in the encoding

    #One idea I have is putting the information at the beginnign of the string
    #So when you encode the first number of the string is how many spaces there are and then the numbers that follow after it are the lenght of each of those strings. The first number defines how many numbers after it to check.

    def encode(self, strs: List[str]) -> str:
        #length of string
        answerStr = ""
        for string in strs:
            stringLength = str(len(string))
            digits = str(len(stringLength))
            answerStr += digits
            answerStr += stringLength
            answerStr += string
        
        print(answerStr)
        return answerStr


    def decode(self, s: str) -> List[str]:
        start = 0
        answerStr = []
        while start < len(s):
            numDigits = int(s[start])
            start +=1
            number = int(s[start: start + numDigits])
            start += numDigits
            tempStr = ""
            for i in range(number):
                tempStr += s[start]
                start +=1
            answerStr.append(tempStr)
        
        return answerStr            


            







        

