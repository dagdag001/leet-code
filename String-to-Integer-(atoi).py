class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if s == \\:  # Handle empty string after stripping
            return 0
        
        negative = False
        index = 0
        
        if s[0] == '-':
            negative = True
            index = 1
        elif s[0] == '+':
            index = 1
        
        num = 0
        for i in range(index, len(s)):
            if s[i] not in \0123456789\:
                break
            num = num * 10 + (ord(s[i]) - 48)
        
        if negative:
            num = -num
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1 #to deal with overloading
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num