class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = cost[0]
        second = cost[1]
        if n > 2:
            for i in range(2,n):
                now = cost[i] + min(first,second)
                first = second
                second = now
        return min(first,second)