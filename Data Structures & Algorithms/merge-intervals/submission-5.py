class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort list by start time
        #compare a.end with b.start to determine if interval is merged
        #have to run while loop if you have concurrent unmerged intervals

        
        #sort intervals by start time
        intervals = sorted(intervals, key=lambda x: x[0])

        #new intervals list
        answer = [intervals[0]]

        for interval in intervals[1:]:
            currStart, currEnd = interval[0], interval[1] 
            currentEndTime = answer[-1][1]
            if currStart <= currentEndTime:
                answer[-1][1] = max(currEnd, currentEndTime)
            else:
                answer.append([currStart, currEnd])
        return answer





        

            

        
             





        