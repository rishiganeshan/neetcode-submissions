import bisect
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        have res = []
        iterate over intevals
            see where it fits in res and update res
        """
        intervals.sort()
        res = []

        

        for interval in intervals:
            if not res or interval[0] > res[-1][-1]:
                res.append(interval)

            elif interval[0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1],interval[1])
            

        return res



        