class Solution:
    def isValid(self, s: str) -> bool:
        parDict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        currStack = []

        if len(s) % 2 != 0:
            return False

        for i in range(0, len(s)):
            if s[i] in parDict:
                currStack.append(s[i])
            elif currStack and parDict[currStack[-1]] == s[i]:
                currStack.pop()
            else:
                return False # added, if the closing bracket does not match or stack is empty
        
        return len(currStack) == 0