# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def IsPopOrder(self, pushV, popV):
        stack = []
        pop_idx = 0
        for item in pushV:
            stack.append(item)
            while stack and stack[-1] == popV[pop_idx]:
                stack.pop()
                pop_idx += 1
        if stack:
            return False
        return True


s = Solution()
print(s.IsPopOrder([5, 2, 3, 7], [3, 5, 2, 7]))
