class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev, current = 0,0
        for num in nums[1:]:
            new = max(prev+num,current)
            prev, current = current, new
        res = current
        prev, current = 0,0
        for num in nums[:-1]:
            new = max(prev+num,current)
            prev, current = current, new
        res = max(res, current)

        return res
            
        