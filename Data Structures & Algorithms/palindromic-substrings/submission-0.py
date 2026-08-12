class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPalindromeFrom(i,j):
            nonlocal res
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
        
        n = len(s)

        for i in range(n):
            countPalindromeFrom(i,i)
            countPalindromeFrom(i,i+1)
        
        return res
            


        