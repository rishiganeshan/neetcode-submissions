from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = defaultdict(int)
        fmap = defaultdict(list)
        topk = []

        for num in nums:
            counter[num] += 1
        
        for num, freq in counter.items():
            fmap[freq].append(num)
        
        for freq in range(len(nums), 0, -1):
            if freq in fmap:
                for num in fmap[freq]:
                    k -= 1
                    topk.append(num)
                if k == 0:
                    break

        return topk

