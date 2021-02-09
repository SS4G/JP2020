from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0x01 << len(nums)):
            res.append(self.map_func(nums, i))
        return res

    def map_func(self, nums, bit_n):
        res = []
        for i in range(len(nums)):
            if bit_n & (0x01 << i):
                res.append(nums[i])
        return res