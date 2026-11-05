class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #Because you get k number of replacements, your window length is
        # num of valid characters + k invalid characters

        #Use a dictionary of counts to keep track of the window

        counts = {}
        answer = 0
        left = 0
        for right in range(0, len(s)):

            #adding to dictionary
            if s[right] not in counts:
                counts[s[right]] = 1
            else:
                counts[s[right]] +=1

            maxCount = max(counts.values())

            while maxCount + k < right - left + 1:
                counts[s[left]] -=1
                left +=1
            
            answer = max(answer, right - left + 1)

        return answer

            

            
        