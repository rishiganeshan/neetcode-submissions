class Solution:
    def numDecodings(self, s: str) -> int:

        prevprev = 0
        prev = 1
        prevChar = "0"

        for char in s:
            cur = 0
            if char != "0":
                cur += prev
            if 10 <= int(prevChar + char) <= 26:
                cur += prevprev
            
            prevprev, prev, prevChar = prev, cur, char
        
        return cur




        