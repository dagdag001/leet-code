from collections import Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_bracket = 0
        single_close_bracket = 0
        for i in s:
            if i == "(":
                open_bracket+=1
            elif i == ')':
                if open_bracket > 0:
                    open_bracket-=1
                else:
                    single_close_bracket+=1
        return open_bracket + single_close_bracket
                
