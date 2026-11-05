"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


            #Sweep Line Algorithim
            #Create a dict that stores each event. If it's a start event, then its value is +1.
            #If its a end event, then its value will be a -1

            eventsDict = defaultdict(int) #Basically initalizes values that don't exist in dict to 0

            for interval in intervals:
                eventsDict[interval.start] +=1
                eventsDict[interval.end] -=1
            

            #To sort dictionaries in python, use the sorted() method
            answer = 0
            currNumMeetings = 0

            for event in sorted(eventsDict.keys()):
                currNumMeetings += eventsDict[event]
                answer = max(answer, currNumMeetings)
            
            return answer





        