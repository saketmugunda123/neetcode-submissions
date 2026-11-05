"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        #The goal is to figure out the most concurrent meetings at one time

        #Think about event based processing. Each start/end is an event. Start is a +1
        #end is a -1. 
        from collections import Counter

        eventsDict = Counter()

        for interval in intervals:
            eventsDict[interval.start] +=1
            eventsDict[interval.end] -=1

        #Now simply iterate through the sorted version of the dict
        maxValue = 0
        temp = 0
        for key in sorted(eventsDict):
            temp += eventsDict[key]
            maxValue = max(temp, maxValue)
        return maxValue

        