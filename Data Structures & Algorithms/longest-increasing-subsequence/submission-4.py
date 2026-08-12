import bisect
from math import inf
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        
        even better using just nums (need a way to mark each one we've seen though)
        nums[i] = min num to get a sequence of length i+1
        res = 0
        for i in range(1,len(nums)):
            num = nums[i]
            nums[i] = inf

            for j in range(i-1,-1,-1):
                prevNum = nums[j]
                if prevNum < num < nums[j+1]:
                    nums[j+1] = num
                    res = max(res,j+2)
        
        return res

        9,1,3,2,3,3,7
        i,i,i,i,i,i,i 9
        9,i,i,i,i,i,i 1
        1,i,i,i,i,i,i 3
        1,3,i,i,i,i,i 2
        1,2,i,i,i,i,i 3
        1,2,3,i,i,i,i 3
        1,2,3,i,i,i,i 7
        1,2,3,7,i,i,i

        we look for rightmost number the current num is greater than (say it's at idx i), then we update dp[i+1] current num
            
        """

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


        