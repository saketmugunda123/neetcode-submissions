"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


            #create a dict that maps start events to 1 and end events to -1

            eventsDict = defaultdict(int)
            for interval in intervals:
                eventsDict[interval.start] += 1
                eventsDict[interval.end] -=1
            
            count = 0
            answer = 0
            for key in sorted(eventsDict.keys()):
                count += eventsDict[key]
                answer = max(answer, count)
            
            return answer







        