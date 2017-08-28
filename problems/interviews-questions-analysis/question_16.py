# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def rectCover(self, number):
        """
        使用一个2*1的小矩形横着或者竖着来覆盖一个大的的矩形，现在大的矩形为2*n，问无重叠的覆盖大矩形总共
        有多少种覆盖的方法。
        这个问题的第一眼感觉用递归可以解决，因为只要将问题化为原来的更小的问题，就应该可以尝试使用递归的方
        法来解决这个问题。

        """
        state = [0, 1, 2]
        for i in range(3, number+1):
            state.append(state[i-2] + state[i-1])
        return state[number]


s = Solution()
number = 4
print(s.rectCover(number))
