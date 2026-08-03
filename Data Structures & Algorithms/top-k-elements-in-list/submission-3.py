import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(set)
        counter = {}

        for num in nums:
            if num in counter:
                frequencies[counter[num]].remove(num)
                counter[num] += 1
            else:
                counter[num] = 1

            frequencies[counter[num]].add(num)

        res = []

        for i in range(len(nums),-1,-1):
            for num in frequencies[i]:
                res.append(num)
                k -= 1
            if k == 0:
                return res







        