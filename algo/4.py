class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        k = (len(nums1) + len(nums2))
        if k % 2 != 0:
            k = (k >> 1) + 1
            return self.findTopK(nums1, nums2, k)
        else:
            k1 = (k >> 1) + 1
            k2 = (k >> 1)
            return (self.findTopK(nums1, nums2, k1) + self.findTopK(nums1, nums2, k2)) / 2

    def findTopK(self, nums1, nums2, k):
        #print("nums1={} nums2={} k={}".format(nums1, nums2, k))
        if k == 1:
            if len(nums1) > 0 and len(nums2) > 0:
                return min(nums1[0], nums2[0])
            elif len(nums1) > 0:
                return nums1[0]
            else:
                return nums2[0]
        else:
            n1, n2, cutted = self.stripHalfK(nums1, nums2, k)
            k -= cutted
            return self.findTopK(n1, n2, k)

    def stripHalfK(self, nums1, nums2, k):
        half = 0
        if k % 2 == 0:
            half = k >> 1
        else:
            half = (k - 1) >> 1
        #print("nums1={} nums2={} k={} cutted={}".format(nums1, nums2, k, half))
        if len(nums1) < half:
            return nums1, nums2[half:], half
        elif len(nums2) < half:
            return nums2, nums1[half:], half

        if nums1[half - 1] < nums2[half - 1]:
            # cutted_nums1 cutted_nums2 cut_num
            return nums1[half:], nums2, half
        else: # nums2[half] > nums1[half]:
            return nums2[half:], nums1, half

if __name__ == "__main__":
    s = Solution()
    nums1 = []
    nums2 = [2, 4, 6, 8, 10, 11]
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)
