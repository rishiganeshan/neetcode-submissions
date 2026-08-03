class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        if len(strs) == 0:
            return ""

        for s in strs:
            for char in s:
                encoded.append(str(ord(char)))
                encoded.append(" ")
            encoded.append("e")
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        res = []
        curWord = []
        curChar = []

        for char in s:
            if char == "e":
                res.append("".join(curWord))
                curWord = []
            elif char == " ":
                curWord.append(chr(int("".join(curChar))))
                curChar = []
            else:
                curChar.append(char)
                
        return res



        
