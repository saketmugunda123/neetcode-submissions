class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        left = 0
        answer = 0
        for right in range(len(s)):
            #invalid window
            while s[right] in window:
                window.remove(s[left])
                left +=1
            window.add(s[right])
            answer = max(right -left + 1, answer)
        return answer
            
        
        
        
            