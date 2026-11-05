class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #the dictionary will always be the size O(1) so look up is always O(1)
        #keep track of window with counts dictionary. For each window simply check if the less frequent character has less than or equal to k occurances

        window = {}
        left = 0
        answer = 0
        for right in range(0, len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            while (max(window.values()) + k ) < (right - left + 1):
                window[s[left]] -=1
                left +=1
            answer = max(answer, right - left + 1)
        
        return answer
                



            
            