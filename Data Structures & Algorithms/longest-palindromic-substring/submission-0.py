class Solution:
    def longestPalindrome(self, s: str) -> str:

        """
        basic is iterate over each char in s, and then iterate out from there to see how far you can go till not palindrome. needs to account for palindromes with two middle letters e.g. a,a
        """
        res = [0,0]

        def isPalindrome(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            i += 1
            j -= 1
            return (i,j)
        
        for idx in range(len(s)):
            tmp = isPalindrome(idx,idx)
            if tmp[1]-tmp[0]> res[1]-res[0]:
                res = tmp

            tmp = isPalindrome(idx,idx+1)
            if tmp[1]-tmp[0]> res[1]-res[0]:
                res = tmp

        return s[res[0]:res[1]+1]

            



        