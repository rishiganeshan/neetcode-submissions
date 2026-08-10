class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = [0] * 26
        l, r = 0, 0
        res = 0


        
        while r < len(s):
            counter[ord(s[r])-ord('A')] += 1

            if sum(counter) - max(counter) <= k:
                res = max(res,r-l+1)
            else:
                counter[ord(s[l])-ord('A')] -= 1
                l += 1
                
            r += 1
        
        return res

