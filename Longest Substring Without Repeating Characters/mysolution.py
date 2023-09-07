# 9/6/2023
# Alex Knusel

### Problem ###
# Given a string s, find the length of the longest substring without repeating characters.

### Solution ###

# Time-Complexity: O(N)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = ""
        longest = ""
        l, r = 0, 0
        while r != len(s):
            if s[r] not in seen:
                seen += s[r]
                r += 1
            else:
                if len(seen) > len(longest):
                    longest = seen
                    seen = ""
                else:
                    seen = ""
                l += 1
                r = l
        # for cleaning up at end in case the las
        if len(seen) > len(longest):
            longest = seen
        return len(longest)