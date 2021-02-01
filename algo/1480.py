class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        dp = [0,] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i]
        return dp