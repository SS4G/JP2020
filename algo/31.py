class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums
        if len(nums) == 1:
            return
        else:
            op_flag = False
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    changed_part = nums[i:]
                    changed_part.sort
                    op_flag = True
            if not op_flag:
                nums.sort()
            
                        