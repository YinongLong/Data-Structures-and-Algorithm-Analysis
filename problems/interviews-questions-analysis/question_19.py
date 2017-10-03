# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def reOrderArray(self, array):
        length = len(array)
        for i in range(1, length):
            temp_num = array[i]
            if temp_num % 2 == 0:
                continue
            for j in range(i - 1, -1, -1):
                if array[j] % 2 == 0:
                    array[j+1] = array[j]
                else:
                    array[j+1] = temp_num
                    break
            else:
                array[0] = temp_num

        return array


s = Solution()
array = [2,4,6,1,3,5,7]
s.reOrderArray(array)
print(array)
