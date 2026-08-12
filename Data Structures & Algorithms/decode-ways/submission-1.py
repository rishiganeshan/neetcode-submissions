class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        
        dic = {}
        dic["1"] = set([str(i) for i in range(10)])
        dic["2"] = set([str(i) for i in range(7)])

        
        dp_2, dp_1 = 1,1

        prevChar = s[0]

        for i in range(1,n):
            char = s[i]

            dp_0 = 0

            if prevChar in dic and char in dic[prevChar]:
                dp_0 += dp_2

            if char != "0":
                dp_0 += dp_1
            
            dp_2, dp_1, prevChar = dp_1, dp_0, char
        
        return dp_1
            


        