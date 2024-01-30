class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(strs, key=len)
        for i, char in enumerate(m):
            for string in strs:
                if string[i] != char:
                    return m[:i]
        return m                