from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for r in range(len(nums)):
            for s in combinations(nums, r=r):
                res.append(s)
        return res