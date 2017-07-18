# -*- coding: utf-8 -*-
from __future__ import print_function

from collections import defaultdict

class Solution(object):

    def isMatch_DP(self, s, p):
        
        pass

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        p_idx = 0
        s_idx = 0
        star_idx = -1
        match_idx = -1
        while s_idx < s_len:
            if (p_idx < p_len) and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                p_idx += 1
                s_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                p_idx += 1
                match_idx = s_idx
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
            else:
                return False
        while (p_idx < p_len) and (p[p_idx] == '*'):
            p_idx += 1
        return True if p_idx == p_len else False


print('--- start ---')
s = Solution()
result = s.isMatch('abcdefg', 'a*de?*g')
print('--- ending ---')
print(result)
