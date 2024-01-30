class Solution:
    def romanToInt(self, s: str) -> int:
        RomanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        output = RomanDict[s[n-1]]
        for i in range(n-2,-1,-1):
            if RomanDict[s[i]] >= RomanDict[s[i+1]] :
                output += RomanDict[s[i]]
            else:
                output -= RomanDict[s[i]]
        return output   