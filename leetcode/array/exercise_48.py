# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def _get_position(self, radius, odd, x, y):
        if not odd:
            x = x if x < 0 else x - 1
            y = y if y > 0 else y + 1
        j = x + radius
        i = radius - y
        return i, j

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead
        """
        len_mat = len(matrix)
        state_mat = [[False] * len_mat for _ in range(len_mat)]
        odd = False if len_mat % 2 else True
        radius = len_mat / 2
        for i in range(len_mat):
            for j in range(len_mat):
                if state_mat[i][j]: continue
                x = j - radius
                y = radius - i
                if not odd:
                    x = x if x < 0 else x + 1
                    y = y if y > 0 else y - 1
                cur_i, cur_j = i, j
                for _ in range(4):
                    next_x, next_y = -y, x
                    next_i, next_j = self._get_position(radius, odd, next_x, next_y)
                    matrix[cur_i][cur_j], matrix[next_i][next_j] = matrix[next_i][next_j], matrix[cur_i][cur_j]
                    state_mat[cur_i][cur_j] = True
                    cur_i, cur_j = next_i, next_j
                    x, y = next_x, next_y


matrix = [[1, 2], [3, 4]]
s = Solution()
s.rotate(matrix)
print(matrix)
