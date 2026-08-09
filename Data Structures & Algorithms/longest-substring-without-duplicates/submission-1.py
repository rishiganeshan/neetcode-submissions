from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        chars = defaultdict(int)
        l, r = 0, 0
        chars[s[0]] += 1

        while r < len(s):
            if r + 1 < len(s) and len(chars) == r-l+1 and s[r+1] not in chars:
                r += 1
                chars[s[r]] += 1
            else:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
                r += 1
                if r == len(s):
                    break
                chars[s[r]] += 1


        return r-l+1

        