from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        dp[i] = min coins I can use to get a total amount of i
        initalise all dp to inf
        iterate over i from 0 to amount inclusive
            for coin in coins:
                dp[i] = min(dp[i], 1 + dp[i-coin])
        
        if dp[amount] is inf return -1 else return dp[amount]

        might be worth sorting amount in reverse or something, and breaking early not sure if it works
        """

        dp = [inf] * (amount+1)
        dp[0] = 0

        coins.sort()

        """
        0  [0]
        1  [0,i]
        2  [0,i,1]
        3  [0,1,2,3]

        """

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin < 0:
                    break
                dp[i] = min(dp[i], 1 + dp[i-coin])
        
        return -1 if dp[amount] == inf else dp[amount]




        
        