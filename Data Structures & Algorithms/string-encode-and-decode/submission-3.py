class Solution:

    def encode(self, strs: List[str]) -> str:
        e = []
        for s in strs:
            e.append(str(len(s)))
            e.append("-")
            e.append(s)
        return ''.join(e)

    def decode(self, s: str) -> List[str]:
        d = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '-':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            d.append(word)
            i = j+1+length
        return d

