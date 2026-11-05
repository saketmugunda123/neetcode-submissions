class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #Sort the intervals by end time
        intervals = sorted(intervals, key = lambda x: [x[1],-x[0]])
        print(intervals)

        #the idea is that you want to pick the events that finish first
        #so you have as much room as possible to make decisions 
        
        #That means ties should be decided by the ones that starts later bc
        #they take up less space

        if len(intervals) < 2:
            return 0
        
        answerArr = [intervals[0]]
        count = 0
        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            
            #overlap case
            if answerArr[-1][1] > start:
                count +=1 
                continue
            else:
                answerArr.append([start,end])
        return count

        