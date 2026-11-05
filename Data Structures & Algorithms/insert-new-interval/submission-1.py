class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        #first find where start fits 
        startIndex = 0
        while startIndex < len(intervals) and newInterval[0] > intervals[startIndex][1]: 
            startIndex +=1
        
        #start index represents where the merged interval will start
        #end index represents where it will end

        endIndex = 0
        while endIndex < len(intervals) and  newInterval[1] >= intervals[endIndex][0]:
            endIndex +=1 

        if startIndex < endIndex:
            mergedStart = min(intervals[startIndex][0], newInterval[0])
            mergedEnd = max(intervals[endIndex -1 ][1], newInterval[1])
            merged = [mergedStart, mergedEnd]
            return intervals[:startIndex] + [merged] + intervals[endIndex:]
        else:
            return intervals[:startIndex] + [newInterval] + intervals[endIndex:]
