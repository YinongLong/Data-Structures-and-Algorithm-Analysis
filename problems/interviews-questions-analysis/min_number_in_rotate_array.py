# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def minNumberInRotateArray(self, rotateArray):
        """
        找到旋转数组中的最小的一个数字，而这个旋转数组来自于一个非递减数组
        1. 一个简单直观的方法就是从数组的最后一位向前遍历，一旦遇到递增情况，就说明前一个是最小的
        Parameters
        ----------
        rotateArray: List[int]
            旋转数组的数字列表

        Returns
        -------
        minimum: int
            旋转数组中最小的一个数字
        """
        len_array = len(rotateArray)
        pre_number = rotateArray[-1]
        for i in range(-2, -len_array-1, -1):
            if rotateArray[i] > pre_number:
                return pre_number
            else:
                pre_number = rotateArray[i]
        return pre_number


numbers = [3, 4, 5, 1, 2]
s = Solution()
print(s.minNumberInRotateArray(numbers))
