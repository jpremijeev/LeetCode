class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output = []
        output.append(0)
        s = 0
        for i in gain:
            s += i
            output.append(s)
        return max(output)