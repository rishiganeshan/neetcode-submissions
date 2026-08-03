class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = [0]*26

        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            charS[ord(s[idx])-ord('a')] += 1
            charS[ord(t[idx])-ord('a')] -= 1

        for num in charS:
            if num != 0:
                return False
        return True
        