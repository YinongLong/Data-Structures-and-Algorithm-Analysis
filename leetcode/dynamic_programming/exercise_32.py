# -*- coding: utf-8 -*-

from __future__ import print_function

class Solution(object):

    def confirm(self, left_char, right_char):
        if left_char == '(' and right_char == ')':
            return True
        else:
            return False

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = list(s)
        temp_array = []
        matching = True
        while matching:
            matching = False
            s_len = len(s)
            i = 0
            while i < s_len:
                next_index = i + 1
                if next_index >= s_len:
                    temp_array.append(s[i])
                    break
                if s[i] not in ['(', ')']:
                    temp_array.append(s[i])
                    i += 1
                else:
                    another_temp = []
                    while next_index < s_len and (s[next_index] not in ['(', ')']):
                        another_temp.append(s[next_index])
                        next_index += 1
                    if next_index >= s_len:
                        temp_array.append(s[i])
                        temp_array.extend(another_temp)
                        break

                    if self.confirm(s[i], s[next_index]):
                        matching = True
                        temp_array.append(2)
                        temp_array.extend(another_temp)
                        i += (next_index - i) + 1
                    else:
                        temp_array.append(s[i])
                        temp_array.extend(another_temp)
                        i += (next_index - i)
            s = temp_array
            temp_array = []
        maximum = 0
        counter = 0
        for item in s:
            if item in ['(', ')']:
                if counter > maximum:
                    maximum = counter
                counter = 0
            else:
                counter += item

        return maximum if maximum > counter else counter


s = Solution()
nums = s.longestValidParentheses('())())(())())')
print(nums)
