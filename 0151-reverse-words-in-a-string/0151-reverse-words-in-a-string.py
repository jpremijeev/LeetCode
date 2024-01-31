class Solution:
    def reverseWords(self, s: str) -> str:
        a = list(s.split())
        a.reverse()
        b = ' '.join(a)
        return b