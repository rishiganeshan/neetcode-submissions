class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # len(nums) + 1, bit i means i is seen
        bits = 0

        for num in nums:
            mask = (bits >> num) | 1
            bits = bits | (mask << num)
        
        i = 0
        while True:
            if not bits&1:
                return i
            i += 1
            bits >>= 1

        