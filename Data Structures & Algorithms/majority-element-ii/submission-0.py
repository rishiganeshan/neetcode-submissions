from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freqGoal = len(nums) // 3 + 1
        numCounter = defaultdict(int)

        res = []

        # def addNToBit(bit, n):
        #     bit = bit | 1 << n

        # def addNToBit(bit, n):
        #     bit = bit | 1 << n
            

        for num in nums:
            numCounter[num] += 1
            if numCounter[num] == freqGoal:
                res.append(num)

        return res

        


        