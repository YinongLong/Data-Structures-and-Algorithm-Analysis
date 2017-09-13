# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def reOrderArray(self, array):
        start = -1
        for idx, item in enumerate(array):
            if item % 2 == 1:
                start += 1
                if start != idx:
                    array[start], array[idx] = array[idx], array[start]

s = Solution()
array = [1,2,3,4,5,6,7]
s.reOrderArray(array)
print(array)
