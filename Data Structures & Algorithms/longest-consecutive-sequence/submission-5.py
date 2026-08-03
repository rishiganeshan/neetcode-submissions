from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue
            cnt = 1
            while num + 1 in nums:
                num += 1
                cnt += 1
            res = max(cnt,res)
        return res





        