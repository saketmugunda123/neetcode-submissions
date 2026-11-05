class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        tempSet = set()

        left = 0
        answer = 0

        for right in range(0, len(s)):

            while s[right] in tempSet:
                tempSet.remove(s[left])
                left +=1
    

            tempSet.add(s[right])
            answer = max(answer, right - left + 1)
        
        return answer
                
            


        