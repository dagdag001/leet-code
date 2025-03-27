class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        def factorsOf(n):
            factors = []
            for i in range(1,int(n/2) + 1):
                if n %i == 0:
                    factors.append(i)
            factors.append(n)
            return factors
        
        factors = factorsOf(n)
        if k > len(factors): 
            return -1
        else:
            return factors[k-1]
