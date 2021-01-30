import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        valid_set = string.digits + string.ascii_lowercase
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while left < len(s) and s[left] not in valid_set:
                left += 1
            while right >= 0 and s[right] not in valid_set:
                right -= 1
            if right == 0 and left >= len(s):
                return True 
            elif right == 0 or left >= len(s):
                return False
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True