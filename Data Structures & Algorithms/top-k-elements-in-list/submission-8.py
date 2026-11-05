class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        #create a counts dictionary
        counterDict = Counter(nums)

        
        #create a list of size n + 1
        listStorage = [[] for i in range(len(nums)+1)]

        #iterate through values of the counterDict
        for key, val in counterDict.items():
            listStorage[val].append(key)

        answer = []

        for i in range(len(listStorage)-1, -1, -1):
            group = listStorage[i]
            for number in group:
                answer.append(number)
            if len(answer) == k:
                return answer
        return answer
      
        
        