class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []

        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append(" ")
            encoded_str.append(s)

        return "".join(encoded_str)


        

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        idx = 0
        while idx < len(s):
            r = idx + 1
            while s[r] != " ":
                r += 1

            length = int(s[idx:r])
            r += 1
            if length == 0:
                decoded_strs.append("")
            else:
                decoded_strs.append(s[r:r+length])
            idx = r+length

        return decoded_strs
