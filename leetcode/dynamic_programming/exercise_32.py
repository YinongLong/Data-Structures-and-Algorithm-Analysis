# -*- coding: utf-8 -*-

from __future__ import print_function

import array

class Solution(object):

    def longestValidParentheses_stack(self, s):
        """
        这个方法是使用Stack来计算最长有效串，没有用到Dynamic Programming的方法，
        其时间复杂度为O(n)，空间复杂度为O(n)。
        """
        maximum = 0
        stack = []
        stack.append(-1)
        for idx, item in enumerate(s):
            if item == '(':
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    maximum = max(maximum, idx - stack[-1])
        return maximum

    def longestValidParentheses_nn(self, s):
        """
        这个解法来自题目文档中的第一个动态规划的解法，其时间复杂度为O(n)，空间复杂度为O(n)。
        这个解法通过设置一个同s大小一致的dp array来记录在相应的索引位上终止的最大有效串长，首先
        将这个dp array全部设为0，然后遍历s对dp array进行更新，很明显符号'('对应的索引位其计数
        应该一直为0，因为以'('为终止符号的不是有效串，因此只需要更新')'对应的索引位。当更新字符')'
        对应的索引位时，因为其之间位置的最长有效串已经计算出来，因此可以借用前面已经计算出来的结果，
        考虑到')'前的符号只有两种可能，一种是'('；另外一种是')'。如果是前一种情况，那么当前索引位
        （假设其索引为i）对应的最长有效串的长度应该就是s[i] = s[i-2] + 2；如果是后一种情况，那么
        我们需要判断当前符号是否构成了一个有效串，首先前面一位字符构成的有效串长为s[i-1]，那么前面
        一位字符构成的有效串的开始位置应该是i - s[i-1]，那么再往前推一步i - s[i-1] - 1就是用来判
        断是否和当前索引位构成有效串的字符，如果位于i - s[i-1] - 1的字符是'('，就代表构成了有效串，
        那么当前索引位的dp array值应该更新为s[i] = s[i-1] + 2 + s[i - s[i-1] - 2]。这样就可以
        一次性遍历整个s，从而返回最长的有效串长。
        """
        s_len = len(s)
        counter = {}
        maximum = 0
        for idx, char in enumerate(s):
            if char == ')':
                temp_idx = idx - 1
                if temp_idx >= 0:
                    if s[temp_idx] == '(':
                        counter[idx] = counter.get(temp_idx - 1, 0) + 2
                    else:
                        another_idx = idx - counter.get(temp_idx, 0) - 1
                        if another_idx >= 0 and s[another_idx] == '(':
                            counter[idx] = counter.get(temp_idx, 0) + 2 + counter.get(another_idx - 1, 0)
            if counter.get(idx, 0) > maximum:
                maximum = counter.get(idx, 0)
        return maximum

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
nums = s.longestValidParentheses_nn('())())(())()))')
print(nums)
