class Solution:
    def isValid(self, s: str) -> bool:
        
        characterDict = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        
        stack = []

        for char in s:
            if char in characterDict:
                if not stack or stack[-1] != characterDict[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
            
        return len(stack) == 0
