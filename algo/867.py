class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(A[0]) == 0:
            return A
        AT = [[None, ] * len(A) for i in range(len(A[0]))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                AT[j][i] = A[i][j]
        return AT