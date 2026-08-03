class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        calc = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                calc[i] = nums[i]
            else:
                calc[i] = calc[i-1] * nums[i]

            if calc[i] == 0:
                break
        


        agg = 1

        for i in range(len(nums)-1,-1,-1):
            if i == 0:
                calc[i] = agg
            else:
                calc[i] = calc[i-1] * agg
            agg *= nums[i]
        
        return calc


