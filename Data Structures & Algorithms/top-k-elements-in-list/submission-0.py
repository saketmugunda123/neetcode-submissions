class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        if k == 0:
            return []

        
        for i in range(0, len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] +=1


        #Use bucketsort for the counts

        #initalize an empty list of lists
        countsArr = []
        for i in range(0, len(nums) +1):
            countsArr.append([])
        
        for key in counts:
            countsArr[counts[key]] += [key]
        
        answer = []
        for arr in reversed(countsArr):
            if arr == []:
                continue
            for num in arr:
                answer.append(num)
            
            if len(answer) >= k:
                return answer
        return answer


      