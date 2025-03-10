class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = ''
        new_s = []

        while s:
            for i in range(len(s)):
                if s[i] not in newS:
                    newS+=s[i]
                else:
                    break
            s = s[1::] 
            new_s.append(newS)
            newS=''

        longest_substring = \\
        for i in new_s:
            if len(i) > len(longest_substring):
                longest_substring = i  

        return len(longest_substring)
            
