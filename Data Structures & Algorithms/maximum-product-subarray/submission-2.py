from math import inf

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_min_product = 1
        prev_max_product = 1
        res = -11

        for num in nums:

            prev_min_product, prev_max_product = min(prev_min_product*num, prev_max_product*num, num), max(prev_min_product*num, prev_max_product*num, num)

            res = max(res, prev_max_product)

        return res
        