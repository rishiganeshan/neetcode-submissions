class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(arr, goal):
            l,r = 0,len(arr)-1
            pairs = set()
            while l < r:
                if arr[l] + arr[r] > goal:
                    r -= 1
                elif arr[l] + arr[r] < goal:
                    l += 1
                else:
                    pairs.add((arr[l],arr[r]))
                    l += 1
                    r -= 1
            return pairs

        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            pairs = twoSum(nums[idx+1:], -1 * nums[idx])
            for pair in pairs:
                res.append([nums[idx],pair[0],pair[1]])

        return res

            

        