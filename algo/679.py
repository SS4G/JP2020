from operator import add, mul, sub, truediv
from itertools import permutations, product
from functools import reduce
class Solution(object):
    def __init__(self):
        self.ops = {"+": add, "-": sub, "*": mul, "/": truediv}

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.helper(nums)

    def helper(self, nums):
        ops_c = ("+", "-", "*", "/")
        if len(nums) == 1:
            return abs(nums[0] - 24.0) < 1e-6
        else:
            for idx1, idx2 in permutations(range(len(nums)), r=2):
                for op in ops_c:

                    try:
                        tmp_res = self.ops[op](nums[idx1], nums[idx2])
                    except ZeroDivisionError as e:
                        continue

                    new_nums = []
                    new_nums.append(tmp_res)
                    for idx in range(len(nums)):
                        if idx != idx1 and idx != idx2:
                            new_nums.append(nums[idx])
                    if self.helper(new_nums):
                        return True
        return False

if __name__ == "__main__":
    s = Solution()
    #arr = [3,9,7,7]
    arr = [8.0,3.0]
    print(s.judgePoint24(arr))