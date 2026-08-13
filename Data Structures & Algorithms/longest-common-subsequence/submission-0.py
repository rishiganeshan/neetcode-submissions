class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp of len(text1) x len(text2)
        [ , , , , ]
        [ , , , , ]
        [ , , , , ]

        if char1 = char2:
            dp[i][j] = dp[i-1][j-1] + 1
        dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i][j])
             c r a b t
          [0,0,0,0,0,0]
        c [0,1,1, , , ]
        a [0,1, , , , ]
        t [0,1, , , , ]

        [1, , , , ]
        [ , , , , ]
        [ , , , , ]

        """
        # if len(text1) <= tex
        m,n = len(text1),len(text2)

        if m > n:
            text1, text2 = text2, text1
            m,n = n,m

        dp = [0] * (m+1)

        for i in range(1,n+1):
            prev = 0
            for j in range(1,m+1):

                if text1[j-1] == text2[i-1]:
                    prev += 1

                prev, dp[j] = dp[j], max(prev,dp[j-1],dp[j])

        return dp[-1]



        
        