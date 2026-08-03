from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set()
        numset = set(nums)
        seqLength = {}

        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            tmp = num
            length = 1
            while tmp - 1 in numset:
                seen.add(tmp-1)
                if tmp - 1 in seqLength:
                    length += seqLength[tmp-1]
                    break
                else:
                    tmp -= 1
                    length += 1

            seqLength[num] = length
            res = max(res,length)

        
        return res





        