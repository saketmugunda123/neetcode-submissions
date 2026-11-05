class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
       #Create a counts dictionary

        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        


        #Use bucket sort to get answer. Create an array with len(nums)
        #number of empty arrays
        bucketsArray = []
        for i in range(0, len(nums) + 1):
            bucketsArray.append([])
        
        for key in counts:
            bucketsArray[counts[key]].append(key)
        
        
        answerArr = []
        #Iterate through the buckets array backwards to get k most frequent elements
        #Range parameters (start, stop, step)
        for i in range(len(bucketsArray)-1, -1, -1):
            for num in bucketsArray[i]:
                answerArr.append(num)
            if len(answerArr) == k:
                return answerArr





       


      