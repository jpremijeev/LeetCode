class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        if l1>l2:   l = l1
        else: l=l2
        ans = ''
        for i in range(l):
            if i<l1: ans += word1[i]
            if i<l2: ans += word2[i]
        return ans