class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Sort strings and compare

        temp2A = sorted(s)
        temp2B = sorted(t)

        print(temp2A)
        print(temp2B)

        if temp2A == temp2B:
            return True
        return False
