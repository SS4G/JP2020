class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        div = 5
        while div <= n:
            div_num = n // div
            total += div_num
            div *= 5
        return total
            
            