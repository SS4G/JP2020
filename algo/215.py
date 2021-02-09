import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for n in nums:
            heapq.heappush(-k)
        for i in range(k):
            res = heapq.heappop()
            if i == k - 1:
                return -res