class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            b = bin(i)[2:]
            ans.append(b.count('1'))

        return ans        