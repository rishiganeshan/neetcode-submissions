class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        

        carry = 0
        while b:
           
        
            
            carry = MASK&((a&b) << 1)
            a = MASK & a^b
            b = MASK & carry

        return a if a < 2**31 else a-2**32
            

        
    
        