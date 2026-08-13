class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        m,n = max(m,n),min(m,n)

        dp = [0] * (n+2)
        dp[1] = 1

        for _ in range(m-1):
            newDp = [0] * (n+2)
            for i in range(1,n+1):
                newDp[i] = dp[i] + dp[i-1]
            dp = newDp
            # print(dp)

        # print("ok")

        for _ in range(n-1):
            newDp = [0] * (n+2)
            for i in range(n,0,-1):
                newDp[i] = dp[i] + dp[i-1]
            dp = newDp
            # print(dp)

        return dp[-2]

        """
        dp = [0] * (n+2)
        for pos in positions (0,0),(0,1)...(0,m-1):
            newDp = [0] * (n+2)
            for i in range(1,n+1):
                newDp[i] = newDp[i] + newDp[i-1]
            dp = newDp

        (1,m-1),...(n-1,m-1)
        for each pos in position (1,m-1),...(n-1,m-1):
            newDp = [0] * (n+2)

            for i in range(1,n+1):
                newDp[i] = newDp[i] + newDp[i+1]
            dp = newDp


        """
        
        