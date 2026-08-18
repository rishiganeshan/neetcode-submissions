"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        prev = None

        for i in range(len(intervals)):
            if not prev:
                prev = intervals[i]
            else:
                if prev.start <= intervals[i].start < prev.end:
                    return False
                else:
                    prev = intervals[i]

        return True
