class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2)+1)


        for i in range(1,len(text1)+1):
            diag = dp[0]
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    diag, dp[j] = dp[j], diag + 1
                else:
                    diag, dp[j] = dp[j], max(dp[j],dp[j-1])
            
        return dp[-1]


        