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

        #This is event based as at a single timestamp, there are 2 things that can
        #happen: 1. meeting starts. 2. meeting ends. We don't have to check every
        #time in between we simply just have to check what happens at events

        #Event occuring = +1 (new meeting started) event ending = -1 (meeting ended)

        from collections import Counter
        events = Counter()
        for interval in intervals:
            meetingStart, meetingEnd = interval.start,interval.end

            events[meetingStart] +=1
            events[meetingEnd] -= 1
        
        #Iterate through events in order in which they happened so we are doing a 
        #sweep through time
        concurrent = 0
        answer = 0
        for event in sorted(events):
            concurrent += events[event]
            answer = max(answer, concurrent)
        return answer

        