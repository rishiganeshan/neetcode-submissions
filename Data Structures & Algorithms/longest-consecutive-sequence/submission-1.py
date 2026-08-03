from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        arr = nums
        seen = set()
        nums = set(nums)
        seqLength = {}

        for num in arr:
            if num in seen:
                continue
            tmp = num
            length = 1
            while tmp - 1 in nums:
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





        