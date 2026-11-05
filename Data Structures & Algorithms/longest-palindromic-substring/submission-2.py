class Solution:
    def longestPalindrome(self, s: str) -> str:

        #for each node, treat it as teh center. Iterate outwards until no longer a palindrome.
        #Note: you also have to check for even palindromes as well

       

        answer = 0
        stringAnswer = [0,0]
        for i in range(0, len(s)):

            left = i - 1
            right = i + 1

            #check palindrome with odd num of values
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > answer:
                    answer = right - left + 1
                    stringAnswer[0] = left
                    stringAnswer[1] = right
                left -=1
                right +=1
        
            #check palindrome with even num of values
            if i > 0:
                left = i-1
                right = i

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > answer:
                        answer = right - left + 1
                        stringAnswer[0] = left
                        stringAnswer[1] = right
                    left -=1
                    right +=1
        
        return s[stringAnswer[0]:stringAnswer[1] + 1]



        