"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        q = []
        res = 0
        intervals.sort(key=lambda x:x.start)
        for x in intervals:
            a,b = x.start, x.end
            while q and q[0] <= a:
                heapq.heappop(q)
            heapq.heappush(q, b)
            res = max(res, len(q))
        return res