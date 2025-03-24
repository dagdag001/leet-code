class Solution:
    from math import log as log
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        power_five = int(log(n, 5))
        count = 0
        for i in range(1,power_five+1):
            count += n//5**i
        return count