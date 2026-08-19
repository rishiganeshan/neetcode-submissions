class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n+1)
        
        for i in range(1,n+1):
            # print(i)
            dp[i] = dp[i>>1] + (i&1)
            # print(dp[i>>1]+(i&1))
            # print(dp[i])
            # print()

            # print(dp)
            # print(i)
            # print(bin(i))
            # print(bin(i>>1))
            # print("dp")
            # print(i>>1)
            # print(dp[i>>1])
            # print(bin(i&1))
            # print()
        
        return dp