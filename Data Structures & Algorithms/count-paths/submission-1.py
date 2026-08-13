class Solution:
    def uniquePaths(self, m: int, n: int) -> int:



        dp = [1] * (m+1)
        dp[0] = 0
        
        for _ in range(n-1):
            for i in range(1,len(dp)):
                dp[i] += dp[i-1]

        return dp[-1]

        
        