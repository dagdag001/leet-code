class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True 
            x = -1 * x
        xString = str(x)
        xString = xString[::-1]


        intMin = -2**31 
        intMax = (2**31) -1
        if int(xString) > intMax :
            return 0
        if int(xString) < intMin:
            return 0
        if negative:
            return - int(xString)
            
        return int(xString)