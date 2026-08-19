class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if x == 1:
            return 1
        if x == -1:
            return -1 if n%2 == 1 else 1
        cur = 1
        if n < 0:
            while n != 0:
                if cur == 0:
                    return 0
                cur *= (1/x)
                n += 1

        else:
            while n != 0:
                if cur == 0:
                    return 0
                cur *= x
                n -= 1
        
        return cur

        