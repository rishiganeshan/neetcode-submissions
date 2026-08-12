import bisect
from math import inf
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    

        res = 1

        for i in range(1,len(nums)):
            
            num = nums[i]
            nums[i] = inf
            j = bisect.bisect_right(nums, num,hi=res)
            if j > 0 and nums[j-1] == num:
                continue
            res = max(res,j+1)
            nums[j] = num
            # print(nums)
        
        return res


        