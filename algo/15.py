from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum2dict = {}
        val_dict = {}
        results = []
        for i, v in enumerate(nums):
            val_dict.setdefault(v, [])
            val_dict.append(i)

        cnt = Counter(nums)
        if 0 in cnt and cnt[0] >= 3:
            results.append([0, 0, 0])

        for k in cnt:
            if cnt[k] >= 2:
                if -2*k in cnt:
                    results.append([k, k, -2*k])

        kvs = list(cnt.items())

        for i in range(len(kvs)):
            for j in range(i + 1, len(kvs)):
                sum2 = kvs[i][0] + kvs[j][0]
                if -sum2 in cnt:
                    res = [kvs[i], kvs[j], -sum2]
                    results.append(res)
        return results
                    #for v in val_dict[-sum2].values()

