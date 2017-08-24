# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def replaceSpace(self, s):
        """
        :type s: str
        """
        result = []
        for item in s:
            if item == ' ':
                result.append('%20')
            else:
                result.append(item)
        return ''.join(result)


source = 'We are happy'
s = Solution()
print(s.replaceSpace(source))
