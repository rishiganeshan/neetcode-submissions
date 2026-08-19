from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freqGoal = len(nums) // 3 + 1
        numCounter = defaultdict(int)

        res = []
        1,2,3,4,5,6,7,7,7,7

        for i in range(len(nums)):
            num = nums[i]
            if num in res:
                continue
            numCounter[num] += 1
            if numCounter[num] == freqGoal:
                res.append(num)
                del numCounter[num]
            if len(nums) - i - 1 < freqGoal - numCounter[num]:
                del numCounter[num]

        return res



        # nums length to sizes
        # 1->1
        # 2->1,1
        # 3->2
        # 4->2,2
        # 5->2,2
        # 6->3,3
        # 7->3,3
        # 8->3,3
        # 9->4,4
        # 10->4,4
        # 11->4,4
        # 12->5,5










        return res

        


        