from math import inf

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_min_product = 1
        prev_max_product = 1
        res = -11

        for num in nums:

            cur_min_product = min(prev_min_product*num, prev_max_product*num, num)
            cur_max_product = max(prev_min_product*num, prev_max_product*num, num)

            res = max(res, cur_max_product)

            prev_min_product, prev_max_product = cur_min_product, cur_max_product


        return res
        