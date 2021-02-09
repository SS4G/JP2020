
import time
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        left = 0
        right = len(height) - 1
        max_cap = 0
        while left < right:
            cur_cap = (right - left) * min(height[right], height[left])
            max_cap = max(cur_cap, max_cap)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_cap

if __name__ == "__main__":
    arr = list(range(1, 15000))
    s = Solution()
    ts = time.time()
    res = s.maxArea(arr)
    te = time.time()
    print("time={}".format(te - ts))
    print(res)
