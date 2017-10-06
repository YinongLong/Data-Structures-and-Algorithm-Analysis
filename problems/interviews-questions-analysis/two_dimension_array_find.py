# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def find(self, target, array):
        """
        :type target: int
        :type array: List[List[int]]
        :rtype: bool
        """
        height = len(array)
        width = len(array[0])
        posi_x, posi_y = width - 1, 0
        while (posi_x >= 0) and (posi_y < height):
            if array[posi_y][posi_x] == target:
                return True
            elif array[posi_y][posi_x] > target:
                posi_x -= 1
            else:
                posi_y += 1
        return False

array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
target = 7
s = Solution()
print(s.find(target, array))
