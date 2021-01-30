class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0:
            return 0
        if len(cost) < 2:
            return min(cost)

        dp = [None, ] * len(cost) #for i in range(2)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        # dp[i] 从第i个台阶上起跳的最小花费
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])