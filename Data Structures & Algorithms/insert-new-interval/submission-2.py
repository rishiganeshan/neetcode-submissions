from math import inf
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = newInterval
        intervals = [[-inf,-inf]] + intervals + [[inf,inf]]


        l, r = 0, len(intervals)
        lin, rin = False, False

        for idx in range(len(intervals)):
            curStart, curEnd = intervals[idx]

            if curEnd < start < intervals[idx+1][0]:
                l = idx
                break
            elif curStart <= start <= curEnd:
                l = idx
                lin = True
                break
            

        for idx in range(len(intervals)-1,-1,-1):
            curStart, curEnd = intervals[idx]

            if intervals[idx-1][1] < end < curStart:
                r = idx
                break
            elif curStart <= end <= curEnd:
                r = idx
                rin = True
                break


        if lin:
            newInterval[0] = intervals[l][0]
            l -= 1
        if rin:
            newInterval[1] = intervals[r][1]
            r += 1

        # print(intervals)
        # print(l)
        # print(r)
        # print(newInterval)
        # print()
        
        return intervals[1:l+1] + [newInterval] + intervals[r:-1]


        

            
          



        