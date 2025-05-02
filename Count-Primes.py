class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        res =[True] * n
        res[0] = False
        res[1] = False
        for i in range(2, int(n ** 0.5) +1):
            if res[i]:
                j = i
                if res[i] * j > n:
                    break
                while i * j < n:
                    res[i * j] = False
                    j +=1
        return sum(res)