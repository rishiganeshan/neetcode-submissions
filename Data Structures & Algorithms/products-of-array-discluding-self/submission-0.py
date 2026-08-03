class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = [0] * (len(nums) + 2)
        arr[0] = 1
        arr[-1] = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                break
            arr[i+1] = arr[i] * nums[i]

        mlt = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i+1] = arr[i] * mlt
            mlt *= nums[i]
        
        return arr[1:-1]
            

            



        