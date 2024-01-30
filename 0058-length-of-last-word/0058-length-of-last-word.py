class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        else:
            s = s.split(" ")
            return len(s[-1]) 