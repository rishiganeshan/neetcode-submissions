class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        i = 0
        curSum = 0

        def recurse():

            nonlocal i, curSum



            if curSum == target:
                res.append(arr[:])
                return
            if curSum > target or i == len(nums):
                return

            i += 1
            recurse()
            i -= 1
            
            # include, don't increment
            arr.append(nums[i])
            curSum += nums[i]
            recurse()

            arr.pop()
            curSum -= nums[i]
        
        recurse()
        return res







        

        