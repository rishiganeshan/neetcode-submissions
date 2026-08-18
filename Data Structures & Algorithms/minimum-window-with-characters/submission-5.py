class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = [0] * 52

        def getCharIdx(char):
            if "A" <= char <= "Z":
                return ord(char)-ord('A')+26
            else:
                return ord(char)-ord('a')
            
        for char in t:
            counter[getCharIdx(char)] -= 1

        
        def check():
            for num in counter:
                if num < 0:
                    return False
            return True

        l, r = 0,-1
        resl, resr = -1,len(s)
        res = ""

        while r < len(s):
            if check():
                while check() and l <= r:
                    if r - l < resr - resl:
                        resl, resr = l, r

                    counter[getCharIdx(s[l])] -= 1
                    l += 1
                    # print(s[l:r+1])
            else:
                while not check() and r < len(s):
                    r += 1
                    if r == len(s):
                        break
                    # print(s[l:r+1])
                    counter[getCharIdx(s[r])] += 1
                    
        
        if resl == -1:
            return ""
        else:
            return s[resl:resr+1]
            

        
        