# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_length = len(s)
        count = 0
        start = False
        for idx in range(-1, -s_length-1, -1):
            if s[idx] == ' ':
                if start:
                    break
                else:
                    continue
            else:
                start = True
                count += 1
        return count


s = Solution()
print(s.lengthOfLastWord('Hello World! '))
