class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Simply two pointer (one from front and one from back)

        left = 0
        right = len(s) -1

        while left < right:
            if not s[left].isalnum():
                left +=1 
                continue
            if not s[right].isalnum():
                right -=1
                continue
            leftChar = s[left].lower()
            rightChar = s[right].lower()
            if leftChar != rightChar:
                return False
            left +=1
            right -=1
        return True
        