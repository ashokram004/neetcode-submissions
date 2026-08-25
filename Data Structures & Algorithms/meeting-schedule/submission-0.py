"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        curEnd = -1
        for x in intervals:
            a = x.start
            b = x.end
            if a < curEnd:
                return False
            curEnd = max(curEnd, b)
        
        return True