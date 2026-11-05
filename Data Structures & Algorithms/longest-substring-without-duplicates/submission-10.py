class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #your window is simply just a set. The key here is that you shrink the window until there are only unique characters left. You do that by comparing the size of right-left with the size of the set


        window = set()
        left = 0
        answer = 0
        for right in range(0, len(s)):
            if s[right] not in window:
                window.add(s[right])
            else:
                while s[left] != s[right]:
                    window.remove(s[left])
                    left +=1
                window.remove(s[left])
                window.add(s[right])
                left +=1
            
            answer = max(answer, len(window))
        return answer
            