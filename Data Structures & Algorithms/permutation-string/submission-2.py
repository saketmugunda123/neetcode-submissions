class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #fixed window length of s1 and then slide it across. Remember, the dictionary check is O(1) bc at most 26 characters (one for each letter in alphabet)

        from collections import Counter

        need = Counter(s1)
        left = 0
        window = Counter()
        size = len(s1)

        for right in range(len(s2)):
            window[s2[right]] +=1
            
            if right >= size: #this will trigger every time after window=size
                leftChar = s2[right - size]
                window[leftChar] -=1
                if window[leftChar] == 0:
                    del window[leftChar]
                
            if window == need:
                return True
        return False

            

