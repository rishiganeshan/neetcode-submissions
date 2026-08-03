
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        freqs = defaultdict(list)
        for num, cnt in counter.items():
            freqs[cnt].append(num)
        
        res = []

        for cnt in range(len(nums), 0, -1):
            res += freqs[cnt]
            k -= len(freqs[cnt])
            if k == 0:
                return res


