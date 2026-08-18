import bisect
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = []

        
        for i in range(len(intervals)):

            if not res:
                res.append(intervals[i])
            else: 
                if res[-1][0] <= intervals[i][0] < res[-1][1]:
                    if intervals[i][1] < res[-1][-1]:
                        res.pop()
                        res.append(intervals[i])
                else:
                    res.append(intervals[i])

                        
           
        return len(intervals) - len(res)

            
