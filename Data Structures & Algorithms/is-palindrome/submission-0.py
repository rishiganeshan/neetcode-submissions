class Solution:
    def isPalindrome(self, s: str) -> bool:

        # clean the string
        #     make lower case
        #     remove spaces or non alnum chars

        s = s.lower()
        cleanArr = []
        for char in s:
            if char.isalnum():
                cleanArr.append(char)


        l, r = 0, len(cleanArr) - 1
        while l < r:
            if cleanArr[l] != cleanArr[r]:
                return False
            l += 1
            r -= 1
        
        return True