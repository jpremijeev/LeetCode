class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        ans0 = 0
        ans1 = 1
        ans2 = 1
        for i in range(3,n+1):
            ans = ans0 + ans1 + ans2
            ans0 = ans1
            ans1 = ans2
            ans2 = ans
        return ans