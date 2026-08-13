class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res,total = nums[0],nums[0]

        for num in nums[1:]:
            if num > total + num:
                total = num
            else:
                total += num
                
            res = max(res,total)

        return res



        


        