class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # print(res)
            # print(res << 1)
            # print(n&1)
            # print()
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


        