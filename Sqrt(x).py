class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            m = (l+r) // 2
            if m**2  > x:
                r = m-1
            elif m**2 < x:
                l = m +1
               
            else:
                return m
        return r