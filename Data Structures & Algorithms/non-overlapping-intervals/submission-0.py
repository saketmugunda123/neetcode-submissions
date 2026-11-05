class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #First sort the intervals based on start time
        intervals.sort() #This works bc interval isn't an object

        #Idea: When you run into two intervals that overlap, remove the one that ends last
        #That way, you free up more time


        currEndTime = intervals[0][1]
        counter = 0 #Number of meetings we remove
        for i in range(1, len(intervals)):
            start = intervals[i][0]

            if start >= currEndTime: #No overlap exists
                currEndTime = intervals[i][1]
            else:
                counter +=1
                currEndTime = min(currEndTime, intervals[i][1])
        
        return counter

        