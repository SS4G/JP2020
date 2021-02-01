class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = [None for _ in len(A)]
        even_wr = 0
        odd_wr = 1
        for i, a in enumerate(A):
            if i % 2 == 0:
                B[even_wr] = a
                even_wr += 1
            else:
                B[odd_wr] = a
                odd_wr += 1
        return B

