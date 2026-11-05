class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort list by start time
        #compare a.end with b.start to determine if interval is merged
        #have to run while loop if you have concurrent unmerged intervals

        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda x: x[0])
        print(intervals)

        mergedIntervals = []
        mergedIntervals.append(intervals[0])
    

        for i in range(1,len(intervals)):
            #check if it is overlapping w/ end of current merged intervals
            if intervals[i][0] <= mergedIntervals[-1][1]:
                mergedIntervals[-1][1] = max(intervals[i][1], mergedIntervals[-1][1])
            else:
                mergedIntervals.append(intervals[i])
        return mergedIntervals
        

            

        
             





        