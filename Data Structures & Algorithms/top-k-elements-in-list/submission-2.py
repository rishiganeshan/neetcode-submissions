import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        heap = []

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        for num, freq in freq.items():

            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]

        