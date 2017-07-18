# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def isMatch_DP(self, s, p):
        """
        使用DP的方法来进行模式串与源串的匹配，注意DP的思维方式，将子问题的答案存储
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        state_array = []
        for i in range(s_len+1):
            state_array.append([])
            for j in range(p_len+1):
                state_array[-1].append(False)
                
        state_array[0][0] = True
        for idx, char in enumerate(p):
            if char == '*':
                state_array[0][idx+1] = True
            else:
                break
        for s_idx, s_char in enumerate(s):
            for p_idx, p_char in enumerate(p):
                if s_char == p_char or p_char == '?':
                    state_array[s_idx+1][p_idx+1] = state_array[s_idx][p_idx]
                elif p_char == '*':
                    last_s_and_last_p = state_array[s_idx][p_idx]
                    curr_s_and_last_p = state_array[s_idx+1][p_idx]
                    last_s_and_curr_p = state_array[s_idx][p_idx+1]
                    state_array[s_idx+1][p_idx+1] = last_s_and_last_p or curr_s_and_last_p or last_s_and_curr_p
                else:
                    state_array[s_idx+1][p_idx+1] = False
        return state_array[s_len][p_len]

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
result = s.isMatch_DP('aa', '*')
print('--- ending ---')
print(result)
