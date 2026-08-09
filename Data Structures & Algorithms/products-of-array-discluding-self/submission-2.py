class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                arr[i] = nums[i]
            else:
                arr[i] = nums[i] * arr[i-1]

            if arr[i] == 0:
                break
        
        agg = 1
        for i in range(len(nums)-1,-1,-1):
            if i == 0:
                arr[i] = agg
            else:
                arr[i] = arr[i-1] * agg
                agg *= nums[i]

        return arr

