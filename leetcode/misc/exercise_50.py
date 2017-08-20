# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1.0 / x
            n *= -1
        return x * self.myPow(x * x, n/2) if n % 2 else self.myPow(x * x, n/2)


s = Solution()
print(s.myPow(5, 4))
