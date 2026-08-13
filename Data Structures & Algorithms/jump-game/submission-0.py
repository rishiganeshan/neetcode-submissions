class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # keep list which is naturally sorted (descending), of nums indexes that you can acheive true from. See

        
        # dp[-1] = True
        best = len(nums) - 1

        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= best:
                best = i
        
        return best == 0


        