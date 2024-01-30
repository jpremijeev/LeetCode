# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n+1
        while left+1 < right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res > 0:
                left = mid
            else:
                right = mid
        return left
