class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Simply just use a dictionary to count up the occurrances of each number
        #The reason this is O(1) space is because the dictionary can be at max 26 keys

        from collections import Counter

        stringS = Counter(s)
        stringT = Counter(t)

        return stringS == stringT
