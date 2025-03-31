class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def isPerfect(x):
            if x < 0:
                return False
            sqrt = int(x ** 0.5)
            return sqrt ** 2 == x

        if c < 0:
            return False
        if  c==1:
            return True
        for i in range(int(c**0.5)+1):
        
            if isPerfect(c - (i**2)):
                return True 
        return False