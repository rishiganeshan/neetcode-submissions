from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,-1
        res = 0
        counter = defaultdict(int)


        while True:
            if len(counter) == r-l+1:
                res = max(res,r-l+1)
                
                r += 1
                if r == len(s):
                    break
                counter[s[r]] += 1
                
                
            else:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1


        return res

            

        