class Solution:
    def countBits(self, n: int) -> List[int]:

        def getOneCount(num):
            res = 0
            while num:
                num &= (num-1)
                res += 1
            return res

        
        ans = []
        for i in range(n+1):
            ans.append(getOneCount(i))
        return ans
        