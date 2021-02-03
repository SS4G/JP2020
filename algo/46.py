import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.gen_index(nums)

    def gen_index(self, arr):
        if len(arr) == 1:
            return [list(arr),]
        else:
            results = []
            for k in arr:
                all_set = set(arr)
                all_set.remove(k)
                tmp_arr = []
                tmp_arr.append(k)
                for sub_arr in self.gen_index(all_set):
                    copied_arr = copy.copy(tmp_arr)
                    copied_arr.extend(sub_arr)
                    results.append(copied_arr)
            return results
