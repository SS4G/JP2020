class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        cur_set = set()
        max_len = 0
        while r < len(s):
            if s[r] not in cur_set:
                cur_set.add(s[r])
                r += 1
            else:
                while s[l] != s[r]:
                    cur_set.remove(s[l])
                    l += 1
                l += 1
                r += 1
            max_len = max(max_len, r - l)
        return max_len

