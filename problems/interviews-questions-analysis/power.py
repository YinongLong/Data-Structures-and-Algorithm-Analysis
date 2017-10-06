# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent < 0:
            base = 1 / base
            exponent *= -1
        temp = self.power(base, exponent / 2)
        if exponent % 2 == 0:
            return temp * temp
        else:
            return temp * temp * base


s = Solution()
print(s.power(0.4, -3))
