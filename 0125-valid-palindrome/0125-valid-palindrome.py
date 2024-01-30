class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = []
        char = [c.lower() for c in s if c.isalnum()]
        return char == char[::-1]        