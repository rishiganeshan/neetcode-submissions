from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        def isValid():
            for cnt in counter:
                if cnt < 0:
                    return False
            return True
        
        def getIdx(char):
            if ord('a') <= ord(char) <= ord('z'):
                return ord(char) - ord('a')
            else:
                return ord(char) - ord('A') + 26

        counter = [0] * 52
        for char in t:
            counter[getIdx(char)] -= 1
        
        l,r = 0,len(t) - 1

        for char in s[:r]:
            counter[getIdx(char)] += 1

        
        res = ""

        while r < len(s):

            counter[getIdx(s[r])] += 1

            while isValid() and r-l+1 >= len(t):
                if res == "" or len(res) > r-l+1:
                    res = s[l:r+1]
                
                counter[getIdx(s[l])] -= 1
                l += 1
            
            if len(res) == len(t):
                break
    
            r += 1

        
        return res

        