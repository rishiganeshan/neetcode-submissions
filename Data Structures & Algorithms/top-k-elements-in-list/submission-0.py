import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        h = []

        for num, freq in counter.items():
            heapq.heappush(h,(freq,num))

            if len(h) > k:
                heapq.heappop(h)


        return [pair[1] for pair in h]

        
        