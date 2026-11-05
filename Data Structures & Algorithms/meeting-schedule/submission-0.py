"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #First sort the intervals based on the starting values
        #Then keep track how long you are booked for
        #If the booked var is greater than the start of the next one, then return false


        #Here is the sorting syntax
        #the key is a lambda function (anonymous function) that takes interval object (x) are returns
        #x.start and it sorts the x.start values
        intervals.sort(key=lambda x: x.start)

        bookedTill = 0
        for i in range(0, len(intervals)):
            if intervals[i].start >= bookedTill:
                bookedTill = intervals[i].end
            else:
                return False
        
        return True
            




       

