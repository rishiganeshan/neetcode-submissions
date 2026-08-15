import heapq

class MedianFinder:

    def __init__(self):
        # -1 order, biggest num at top
        self.smallq = []
        # normal, smallest num at top, keep this queue >= length of small q
        self.bigq = []

        self.median = None

        
    def rebalance_and_recalc(self):
        while len(self.smallq) - len(self.bigq) > 1:
            heapq.heappush(self.bigq, -1*heapq.heappop(self.smallq))

        while len(self.bigq) > len(self.smallq):
            heapq.heappush(self.smallq, -1*heapq.heappop(self.bigq))
        if len(self.smallq) > len(self.bigq):
            self.median = -self.smallq[0]
        else:
            self.median = (self.bigq[0]-self.smallq[0]) / 2






    def addNum(self, num: int) -> None:
        if self.median is None:
            heapq.heappush(self.smallq, -1*num)


        elif num >= self.median:
            heapq.heappush(self.bigq, num)
        else:
            heapq.heappush(self.smallq, -num)

        self.rebalance_and_recalc()
        

    def findMedian(self) -> float:


        return self.median
        
        