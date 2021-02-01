class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        return self.isPalindrome(s)

    def isPalindrome(self, s, can_recure=True):
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                if can_recure:
                    return self.isPalindrome(s[left:right], can_recure=False) or self.isPalindrome(s[left+1:right+1], can_recure=False)
                else:
                    return False
            left += 1
            right -= 1
        return True
# aaacbcaaaa