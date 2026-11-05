class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #use a set as the window

        

        s1Dict = defaultdict(int)
        for i in range(0, len(s1)):
            s1Dict[s1[i]] +=1
        

        currWindow = defaultdict(int)
        left = 0

        for right in range(0, len(s2)):
            currWindow[s2[right]] +=1

            if currWindow == s1Dict:
                return True

            while currWindow[s2[right]] > s1Dict[s2[right]]:
                currWindow[s2[left]] -=1
                left +=1
        
        return currWindow == s1Dict


        
        
            
            

        